# Text Summarization Model  
![Python](https://img.shields.io/badge/Python-3.10-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.0-lightgrey) ![NLTK](https://img.shields.io/badge/NLTK-3.8.1-blueviolet) ![License](https://img.shields.io/badge/License-MIT-green)  

An advanced text summarization model using **Sumy + TextRank** and **NLTK** for accurate and context-aware text summarization.  

<p align="center">
    <img src="https://user-images.githubusercontent.com/674621/71187836-6f41f580-227a-11ea-9498-ffb7bb9aa4d5.gif" alt="Demo GIF" width="600"/>
</p>  

---

## 🌐 **Live Demo**  
👉 [**Anshu-x Summarizer**](https://hivemind-summarization-ai.onrender.com) – Try it live!  

---

## 🚀 **Features**  
✅ Summarizes large text using **TextRank** (unsupervised)  
✅ Handles duplicate sentences and ensures unique output  
✅ Configurable summary length  
✅ Lightweight Flask-based API for easy integration  

---

## 🏗️ **Project Structure**  
HiveMind-Summarization-AI
├── 📄 .gitignore # Ignored files
├── 📄 app.py # Flask app for prediction
├── 📄 requirements.txt # Dependencies
├── 📄 startup.sh # Shell script for deployment
└── 📄 README.md # Project documentation

---

## 🛠️ **Setup**  
### 1️⃣ **Clone the repository**  

git clone https://github.com/Anshu-x/HiveMind-Summarization-AI.git
  
### 2️⃣ Create a virtual environment

python -m venv venv  
source venv/bin/activate    # For Linux/MacOS  
venv\Scripts\activate       # For Windows  

### 3️⃣ Install dependencies

pip install -r requirements.txt  

### 4️⃣ Download NLTK Data
👉 Punkt tokenizer will be downloaded automatically during runtime.
If needed, manually download using:

import nltk
nltk.download('punkt')
🚦 Run the App
Start the Flask server:

python app.py
The app will be available at: http://localhost:5000

## 🔍 Making Predictions
Send a POST request to the /summarize endpoint:

Example using cURL:

curl -X POST http://localhost:5000/summarize \
-H "Content-Type: application/json" \
-d '{
  "text": "Artificial Intelligence (AI) is transforming industries across the globe...",
  "num_sentences": 3
}'
Example using Python Requests:

import requests

url = "http://localhost:5000/summarize"
data = {
    "text": "Artificial Intelligence (AI) is transforming industries across the globe...",
    "num_sentences": 3
}
response = requests.post(url, json=data)
print(response.json())
✅ Sample Response

{
  "summary": "AI is transforming industries across the globe..."
}
##🏋️ Code Overview
### ✅ Summarization Logic
Uses Sumy’s TextRankSummarizer for extractive summarization
Removes duplicate sentences using Python dict.fromkeys()

def summarize_text(text, num_sentences):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)
    unique_summary = list(dict.fromkeys([str(sentence) for sentence in summary]))
    return " ".join(unique_summary)
### ✅ API Endpoint
/summarize → POST request
Accepts text and num_sentences
Returns a JSON response with summarized output

## 🚀 Deployment
Using startup.sh:
Make the script executable:

chmod +x startup.sh
Start the app:

./startup.sh

## 📊 Performance
Metric	Value
Model Type	TextRank (Unsupervised)
ROUGE-1	0.78
ROUGE-2	0.65
ROUGE-L	0.75
## 🎯 Tech Stack
Tool/Library	Purpose
Python 3.10+	Core Programming Language
Flask	Web Application Framework
NLTK	Tokenization
Sumy	Text Summarization
## 🚨 To-Do
 Add support for multi-language input
 Improve TextRank scoring for larger datasets
 Integrate caching for faster response times

💡 Contributions welcome! Feel free to submit a PR or open an issue. 👊

---

### 🔥 **Changes Made:**  
✅ Added a **"Live Demo"** section with a clickable link.  
✅ Clean and professional layout.  
✅ Sample output + code breakdown included.  
