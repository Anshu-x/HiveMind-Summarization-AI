#!/bin/bash

echo "Downloading NLTK data..."
python -c "import nltk; nltk.download('punkt'); print('NLTK punkt downloaded successfully')"
python -c "import nltk; print(nltk.data.path)"

echo "Starting Flask app..."
exec python app.py
