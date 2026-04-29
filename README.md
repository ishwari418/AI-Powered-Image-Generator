#  AI-Powered Image Generator

A lightweight, cloud-based **text-to-image generation web application** that allows users to generate high-quality AI images from text prompts without requiring a local GPU.

---

##  Project Overview

**AI-Powered Image Generator** leverages cloud-hosted Stable Diffusion models to generate images in real time.  
All heavy computation is handled remotely, making the system fast, accessible, and easy to use on any machine.

### Key Highlights
- No local GPU required (cloud-based inference)
- Clean and simple UI built with Streamlit
- Fast image generation (typically under 5 seconds)
- Supports styles, negative prompts, and seed values
- Minimal setup (Python 3.8+ only)

---

##  How It Works

### Architecture Flow

User Input (Web UI)
↓
app.py (Streamlit Interface)
↓
generator.py (API Handler)
↓
Pollinations.ai API
↓
Stable Diffusion (Cloud GPU)
↓
Generated Image
↓
Displayed & Downloaded in UI


### Execution Steps  
- User enters a text prompt and optional parameters
- Input is processed and validated
- Request is sent to Pollinations.ai API
- Stable Diffusion runs on remote GPUs
- Image is generated and returned
- Result is displayed and downloadable

---

##  Technology Stack

| Component | Technology | Purpose |
|--------|-----------|--------|
| Language | Python 3.8+ | Core application logic |
| Web UI | Streamlit | Interactive frontend |
| API Calls | Requests | Communication with Pollinations.ai |
| Image Handling | Pillow (PIL) | Image processing |
| AI Model | Stable Diffusion | Image generation |
| Execution | Cloud-based | No local inference |

---

##  Project Structure

AI-Powered-Image-Generator/
├── app.py
├── generator.py
├── utils.py
├── requirements.txt
├── Screenshot (46).png
└── README.md


### File Descriptions

#### app.py
- Builds the Streamlit interface
- Handles user inputs (prompt, style, seed)
- Triggers image generation
- Displays and enables image downloads

#### generator.py
- Communicates with Pollinations.ai API
- Constructs API requests
- Handles responses and errors
- Returns generated image data

#### utils.py
- Input validation helpers
- Image processing and saving
- Common utility functions

---

##  Dependencies & Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Active internet connection

### Installation
```bash
git clone https://github.com/ishwari418/AI-Powered-Image-Generator.git
cd AI-Powered-Image-Generator
pip install -r requirements.txt

 **Run the Application**
streamlit run app.py

Access the app at:
http://localhost:8501

**System Requirements**
| Requirement | Specification         |
| ----------- | --------------------- |
| CPU         | Any modern processor  |
| GPU         | Not required          |
| RAM         | 4 GB or more          |
| Storage     | Less than 100 MB      |
| OS          | Windows, macOS, Linux |
| Internet    | Required              |

**Usage Guide**
Launch the application
Enter an image prompt
Example:

A futuristic city at sunset with flying cars

Select a style (optional)

Add a negative prompt (optional)
Example:
blurry, low quality, distorted

Set a seed (optional)

Click Generate Image

Download the result

**Quick Start**
pip install -r requirements.txt
streamlit run app.py

Example Prompt:
A cyberpunk warrior in a neon-lit city, ultra-detailed, 8k, photorealistic

