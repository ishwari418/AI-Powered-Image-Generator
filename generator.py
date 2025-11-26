import requests
import io
from PIL import Image
import logging
import urllib.parse
import random

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageGenerator:
    def __init__(self):
        self.base_url = "https://image.pollinations.ai/prompt/"
        logger.info("Initializing ImageGenerator with Pollinations.ai")

    def generate(self, prompt, negative_prompt=None, seed=None, width=1024, height=1024):
        """
        Generates an image using the Pollinations.ai API.
        """
        # Pollinations puts the prompt in the URL
        # We can append params like ?seed=123&width=1024
        
        if seed is None:
            seed = random.randint(0, 1000000)
            
        # Construct URL
        # Append negative prompt to prompt if supported, or just rely on prompt engineering
        # Pollinations usually takes just the prompt. 
        # We can try "prompt --no negative_prompt" style if supported, but simple is better.
        # Let's just use the prompt.
        
        full_prompt = prompt
        if negative_prompt:
             full_prompt += f" --no {negative_prompt}"
             
        encoded_prompt = urllib.parse.quote(full_prompt)
        
        url = f"{self.base_url}{encoded_prompt}?seed={seed}&width={width}&height={height}&nologo=true"
        
        try:
            logger.info(f"Sending request to Pollinations.ai: {url}")
            response = requests.get(url)
            
            if response.status_code != 200:
                error_msg = f"API Error {response.status_code}: {response.text}"
                logger.error(error_msg)
                raise Exception(error_msg)
                
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))
            return image
            
        except Exception as e:
            logger.error(f"Error during generation: {e}")
            raise e
