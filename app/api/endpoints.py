from fastapi import APIRouter
from pydantic import BaseModel
from app.core.text_processing import process_text
from app.core.search import search


router = APIRouter()


class TextRequest(BaseModel):
    text: str


@router.post("/process/")
async def process_text_api(request: TextRequest):
    tokens = process_text(request.text)
    return {"tokens": tokens}


@router.post("/search/")
async def search_api(request: TextRequest):
    results = search(request.text)
    return {"results": results}
