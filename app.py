from flask import Flask, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

app = Flask(__name__)

def summarize_text(text, num_sentences):
    # Validate input
    if not text or not isinstance(text, str):
        raise ValueError("Invalid input. Please provide a valid text string.")
    
    # Preprocess and summarize text with TextRank
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = TextRankSummarizer()
    summary = summarizer(parser.document, num_sentences)  # Summarize to the specified number of sentences

    # Remove duplicate sentences
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
        num_sentences = data.get('num_sentences', 12)  # Default to 12 sentences if not specified
        summary = summarize_text(text, num_sentences)
        return jsonify(summary=summary)
    except ValueError as ve:
        return jsonify(error=str(ve)), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
