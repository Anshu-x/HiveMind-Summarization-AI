#!/bin/bash

# Ensure nltk punkt tokenizer is available
python -c "import nltk; nltk.download('punkt')"

# Run the Flask app
python app.py
