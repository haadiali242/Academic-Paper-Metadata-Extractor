# Academic Paper Metadata Extractor

Extract title, authors, references, and abstract from academic PDF papers with ease.

## Overview

This API service extracts structured metadata from academic papers uploaded as PDF files. It leverages Python, FastAPI, and PyMuPDF to parse PDF content and return organized JSON data containing key paper information.

## Features

- Extract paper title
- Identify authors and affiliations
- Parse references and bibliography
- Extract abstract section
- Return structured JSON response
- RESTful API endpoints

## Project Structure

```
.
├── main.py         # API endpoints
├── pdf_parser.py   # PDF extraction logic
├── schema.py       # Response models
├── tests/          # Test files
└── README.md       # This file
```

## Requirements

- Python 3.7+
- FastAPI
- PyMuPDF (fitz)
- uvicorn (for running the server)

## Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install fastapi uvicorn pymupdf
```

## Running the Application

1. Start the development server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

## API Endpoints

### Upload and Extract Metadata

**POST** `/extract`

Upload a PDF file to extract metadata.

Example request:
```bash
curl -X POST "http://localhost:8000/extract" -F "file=@paper.pdf"
```

Example response:
```json
{
  "title": "Machine Learning Approaches for Natural Language Processing",
  "authors": [
    "John Smith",
    "Emily Johnson"
  ],
  "abstract": "This paper presents a comprehensive study of machine learning techniques applied to natural language processing tasks...",
  "references": [
    "Smith, J. (2020). Deep learning for NLP. Journal of AI Research, 15(2), 123-145.",
    "Johnson, E. & Brown, T. (2019). Neural networks in linguistics. Computational Linguistics, 45(3), 67-89."
  ]
}
```

### Get Available Endpoints

**GET** `/`

Get information about available API endpoints.

## Usage Examples

### Using Python requests
```python
import requests

url = "http://localhost:8000/extract"
files = {'file': open('paper.pdf', 'rb')}
response = requests.post(url, files=files)
print(response.json())
```

### Using curl
```bash
curl -X POST "http://localhost:8000/extract" \
  -F "file=@paper.pdf" \
  -H "Content-Type: multipart/form-data"
```

## Testing

Run tests using:
```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

MIT License

## Author

Haadi Ali - CrumWorld Team
