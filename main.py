from fastapi import FastAPI, UploadFile, File
from typing import List
from schema import PaperMetadata
import pdf_parser

app = FastAPI(title="Academic Paper Metadata Extractor")

@app.get("/")
async def root():
    return {
        "message": "Academic Paper Metadata Extractor API",
        "endpoints": {
            "POST /extract": "Extract metadata from uploaded PDF"
        }
    }

@app.post("/extract", response_model=PaperMetadata)
async def extract_metadata(file: UploadFile = File(...)):
    content = await file.read()
    return pdf_parser.extract_metadata(content)
