import streamlit as st
from generator import ImageGenerator
from utils import save_image
import random

# Page configuration
st.set_page_config(
    page_title="Text-to-Image Generator (Pollinations)",
    page_icon="🎨",
    layout="wide"
)

# Initialize generator
if "generator_pollinations" not in st.session_state:
    st.session_state.generator_pollinations = ImageGenerator()

def main():
    st.title("🎨 AI Text-to-Image Generator")
    st.markdown("Generate high-quality images instantly using **Pollinations.ai** (Free & Fast).")

    # Sidebar controls
    with st.sidebar:
        st.header("Settings")
        
        seed = st.number_input("Seed (Optional)", value=None, step=1, help="Leave empty for random results.")
        
        st.markdown("---")
        st.info("Running on: **Pollinations.ai Cloud**")

    # Main content
    col1, col2 = st.columns([1, 1])
    
    # Style Presets
    style_presets = {
        "None": "",
        "Cinematic": ", cinematic lighting, highly detailed, 8k, photorealistic",
        "Anime": ", anime style, studio ghibli, vibrant colors",
        "Digital Art": ", digital art, trending on artstation, concept art",
        "Oil Painting": ", oil painting, textured, classic art style",
        "Cyberpunk": ", cyberpunk, neon lights, futuristic, dark atmosphere",
        "3D Render": ", 3d render, unreal engine 5, octane render"
    }
    
    with col1:
        st.subheader("Prompt Input")
        
        selected_style = st.selectbox("Style Preset", options=list(style_presets.keys()))
        
        prompt_input = st.text_area(
            "Enter your prompt:", 
            height=100, 
            placeholder="A futuristic city at sunset..."
        )
        
        # Append style to prompt
        full_prompt = prompt_input + style_presets[selected_style] if prompt_input else ""
        
        if selected_style != "None" and prompt_input:
            st.caption(f"Full Prompt: {full_prompt}")
        
        negative_prompt = st.text_input(
            "Negative Prompt (Optional):", 
            placeholder="blurry, bad quality, distorted..."
        )
        
        generate_btn = st.button("Generate Image", type="primary")

    with col2:
        st.subheader("Result")
        if generate_btn and prompt_input:
            with st.spinner("Generating image..."):
                try:
                    # Generate image
                    image = st.session_state.generator_pollinations.generate(
                        prompt=full_prompt,
                        negative_prompt=negative_prompt if negative_prompt else None,
                        seed=int(seed) if seed else None
                    )
                    
                    # Display image
                    st.image(image, caption="Generated Image", use_container_width=True)
                    
                    # Save image with metadata
                    metadata = {
                        "negative_prompt": negative_prompt,
                        "seed": int(seed) if seed else "Random",
                        "style_preset": selected_style,
                        "source": "Pollinations.ai"
                    }
                    filepath = save_image(image, full_prompt, metadata)
                    st.success(f"Image saved to: `{filepath}`")
                    
                    # Download button
                    from io import BytesIO
                    buf = BytesIO()
                    image.save(buf, format="PNG")
                    byte_im = buf.getvalue()
                    
                    st.download_button(
                        label="Download Image",
                        data=byte_im,
                        file_name="generated_image.png",
                        mime="image/png"
                    )
                    
                except Exception as e:
                    st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
