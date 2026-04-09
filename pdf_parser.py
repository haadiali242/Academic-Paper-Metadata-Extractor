import fitz  # PyMuPDF
from typing import Dict, List, Optional
import io

def extract_metadata(pdf_content: bytes) -> Dict:
    """
    Extract metadata from academic paper PDF
    
    Args:
        pdf_content: Bytes of the PDF file
        
    Returns:
        Dictionary containing paper metadata
    """
    # Open the PDF from bytes
    pdf_stream = io.BytesIO(pdf_content)
    doc = fitz.open(stream=pdf_stream, filetype="pdf")
    
    # Extract title (usually first page)
    title = "Unknown Title"
    if doc.page_count > 0:
        first_page = doc.load_page(0)
        text = first_page.get_text()
        
        # Simple approach to find title - look for text that might be title
        lines = text.split('\n')
        for line in lines[:10]:  # Check first 10 lines
            # Skip very short lines and empty lines
            if len(line.strip()) > 10 and not line.strip().startswith('Abstract'):
                title = line.strip()
                break
    
    # Extract authors (look in first few pages)
    authors = []
    for i in range(min(3, doc.page_count)):
        page = doc.load_page(i)
        text = page.get_text()
        
        # Look for author-related patterns
        lines = text.split('\n')
        for line in lines:
            if 'author' in line.lower() or 'authors' in line.lower():
                # Get the line after author
                index = lines.index(line)
                if index + 1 < len(lines):
                    authors.append(lines[index + 1].strip())
                break
    
    # Extract abstract
    abstract = None
    # Search through all pages for abstract section
    full_text = doc.get_text()
    abstract_start = full_text.lower().find('abstract')
    if abstract_start != -1:
        abstract_end = full_text.find('\n\n', abstract_start)
        if abstract_end != -1:
            abstract = full_text[abstract_start:abstract_end].strip()
    
    # Extract references
    references = []
    full_text = doc.get_text()
    
    # Simple reference extraction - look for common patterns
    lines = full_text.split('\n')
    reference_section = False
    
    for line in lines:
        # Look for reference section markers
        if any(keyword in line.lower() for keyword in ['references', 'bibliography', 'bibliography']):
            reference_section = True
            continue
            
        if reference_section:
            # Check if this line looks like a reference
            if line.strip() and not line.strip().startswith(('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')):
                if len(line.strip()) > 10:  # Filter out very short lines
                    references.append(line.strip())
            
            # If we hit a new section, stop collecting references
            if any(keyword in line.lower() for keyword in ['introduction', 'conclusion', 'acknowledgments']):
                break
    
    # Close the document
    doc.close()
    
    return {
        "title": title,
        "authors": authors,
        "abstract": abstract,
        "references": references
    }
