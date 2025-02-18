from flask import Flask, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
import os

app = Flask(__name__)

def summarize_text(text, num_sentences):
    if not text or not isinstance(text, str):
        raise ValueError("Invalid input. Please provide a valid text string.")
    
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)

    unique_summary = list(dict.fromkeys([str(sentence) for sentence in summary]))
    summary_text = " ".join(unique_summary)
    return summary_text

@app.route('/')
def home():
    return jsonify(message="Chat Summarizer API is running! Use the /summarize endpoint to summarize text.")

@app.route('/summarize', methods=['POST'])
def summarize_endpoint():
    try:
        data = request.json
        text = data.get('text', '')
        num_sentences = data.get('num_sentences', 12)

        if not text.strip():
            return jsonify(error="Text cannot be empty"), 400

        summary = summarize_text(text, num_sentences)
        return jsonify(summary=summary)
    except ValueError as ve:
        return jsonify(error=str(ve)), 400
    except Exception as e:
        return jsonify(error="An error occurred during summarization. " + str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
