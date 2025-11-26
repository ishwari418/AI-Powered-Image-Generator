import os
from datetime import datetime
from PIL import Image

def create_output_folder(base_path="generated_images"):
    """Creates the output folder if it doesn't exist."""
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    return base_path

import json

def save_image(image, prompt, metadata=None, base_path="generated_images"):
    """
    Saves the generated image with a timestamped filename and associated metadata.
    
    Args:
        image (PIL.Image): The generated image.
        prompt (str): The prompt used to generate the image.
        metadata (dict): Additional metadata to save (seed, steps, etc.).
        base_path (str): The directory to save the image in.
        
    Returns:
        str: The full path to the saved image.
    """
    create_output_folder(base_path)
    
    # Sanitize prompt for filename
    sanitized_prompt = "".join(c for c in prompt if c.isalnum() or c in (' ', '-', '_')).strip()[:50]
    sanitized_prompt = sanitized_prompt.replace(' ', '_')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_base = f"{timestamp}_{sanitized_prompt}"
    
    # Save Image
    image_path = os.path.join(base_path, f"{filename_base}.png")
    image.save(image_path)
    
    # Save Metadata
    if metadata:
        metadata['prompt'] = prompt
        metadata['timestamp'] = timestamp
        json_path = os.path.join(base_path, f"{filename_base}.json")
        with open(json_path, 'w') as f:
            json.dump(metadata, f, indent=4)
            
    return image_path
