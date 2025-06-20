import nltk
nltk.download('stopwords')
nltk.download('punkt_tab')

from transformers import AutoTokenizer, pipeline
from rake_nltk import Rake
import gradio as gr

# 1️⃣ Load slow tokenizers to avoid SentencePiece→fast conversion
t5_tokenizer = AutoTokenizer.from_pretrained(
    "Michau/t5-base-en-generate-headline",
    use_fast=False
)
bart_tokenizer = AutoTokenizer.from_pretrained(
    "facebook/bart-large-cnn",
    use_fast=False
)

# 2️⃣ Initialize the same pipelines you used in Colab
title_generator = pipeline(
    "text2text-generation",
    model="Michau/t5-base-en-generate-headline",
    tokenizer=t5_tokenizer,
)

desc_generator = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    tokenizer=bart_tokenizer,
)

# 3️⃣ Keyword/tag extractor (identical to notebook)
def extract_tags(text, num=5):
    rake = Rake()
    rake.extract_keywords_from_text(text)
    phrases = rake.get_ranked_phrases()[:num]
    hashtags = ["#" + p.replace(" ", "") for p in phrases]
    tags     = [p.replace(" ", "") for p in phrases]
    return hashtags, tags

# 4️⃣ Main processing function
def generate_for_video(video_text):
    if not video_text.strip():
        return "❌ Please paste your script or summary.", "", "", ""

    # Title generation
    title_out = title_generator(
        "headline: " + video_text,
        max_new_tokens=70,
        clean_up_tokenization_spaces=True,
        do_sample=False
    )
    title_text = title_out[0]["generated_text"]

    # Description generation
    desc_out = desc_generator(
        video_text,
        max_new_tokens=150,
        do_sample=False
    )
    desc_text = desc_out[0]["summary_text"]

    # Hashtags & tags
    hashtags, tags = extract_tags(video_text)

    return title_text, desc_text, ", ".join(hashtags), ", ".join(tags)

# 5️⃣ Build Gradio interface
app = gr.Interface(
    fn=generate_for_video,
    inputs=gr.Textbox(
        lines=8,
        placeholder="Paste your video script or summary here…",
        label="Video Script / Summary"
    ),
    outputs=[
        gr.Textbox(label="Generated Title"),
        gr.Textbox(label="Generated Description"),
        gr.Textbox(label="Suggested Hashtags"),
        gr.Textbox(label="Suggested Video Tags"),
    ],
    title="YouTube Title & Description Generator",
    description=(
        "Paste your script/summary and click **Submit**. "
        "This uses Michau/t5-base-en-generate-headline for titles "
        "and facebook/bart-large-cnn for descriptions."
    ),
    allow_flagging="never",
)

if __name__ == "__main__":
    app.launch()