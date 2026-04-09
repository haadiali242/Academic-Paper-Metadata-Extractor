from pydantic import BaseModel
from typing import List, Optional

class PaperMetadata(BaseModel):
    title: str
    authors: List[str]
    abstract: Optional[str] = None
    references: List[str]
