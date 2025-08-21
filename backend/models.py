from pydantic import BaseModel
from typing import Optional

class OcrResponse(BaseModel):
    id: str
    text: str
    title: str
    saved_text_path: str

class GenerateCardRequest(BaseModel):
    id: Optional[str] = None
    text: Optional[str] = None

class GenerateCardResponse(BaseModel):
    id: str
    tech_card_path: str
    title: str
