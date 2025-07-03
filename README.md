# YouTube Title & Description Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Hugging Face Spaces](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-brightgreen)](https://huggingface.co/spaces/SujalChhajed925/yt-title-desc-generator)  
[![GitHub stars](https://img.shields.io/github/stars/Dragonballsuper-1995/yt-title-desc-generator)](https://github.com/Dragonballsuper-1995/yt-title-desc-generator/stargazers)

An **AI‑powered** tool that generates **SEO‑optimized YouTube video titles**, **engaging descriptions**, and **relevant hashtags & tags** from your video script or summary—no manual brainstorming required.

## 🚀 Live Demo

➡️ [https://huggingface.co/spaces/SujalChhajed925/yt-title-desc-generator](https://huggingface.co/spaces/SujalChhajed925/yt-title-desc-generator)

## 📂 Repository Structure

yt-title-desc-generator/
├── app.py # Main Gradio application
├── requirements.txt # Python dependencies
├── README.md # Project overview & setup instructions
└── LICENSE # MIT License

markdown
Copy
Edit

## 🛠️ Features

- **Title Generation**  
  Uses a T5-based transformer (Michau/t5-base-en-generate-headline) to craft catchy, keyword-rich titles under 70 characters.

- **Description Generation**  
  Leverages BART (`facebook/bart-large-cnn`) to produce concise, SEO‑friendly descriptions (100–150 words).

- **Hashtag & Tag Extraction**  
  Applies the RAKE algorithm to pull out top keywords and format them as YouTube hashtags and video tags.

- **Web Interface**  
  Interactive Gradio frontend—paste your script/summary, click **Submit**, and get instant results.

## ⚙️ Installation & Local Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/Dragonballsuper-1995/yt-title-desc-generator.git
   cd yt-title-desc-generator
Create & activate a virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
python app.py
Then open your browser at http://localhost:7860.

📦 Deployment
Hugging Face Spaces
Fork or push this repository to your Hugging Face account.

Create a new Space, choose Gradio as the SDK.

Point it at this repo’s main branch.

Wait for the build to complete and share your Space URL!

🧪 Testing
Use the following sample input to see how it performs:

css
Copy
Edit
Learn how to bake the perfect sourdough loaf at home.
I’ll walk you through creating and feeding your starter,
mixing the dough, bulk fermentation, shaping, and scoring—
plus, tips for achieving a crisp crust and airy crumb.
Ideal for both beginners and experienced bakers.
🤝 Contributing
Fork the repo

Create a feature branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m "Add awesome feature")

Push to your branch (git push origin feature/YourFeature)

Open a pull request
