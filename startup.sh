#!/bin/bash

echo "Downloading NLTK data..."
python -c "import nltk; nltk.download('punkt'); print('NLTK punkt downloaded successfully')"

echo "Starting Flask app..."
exec python app.py
