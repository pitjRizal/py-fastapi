from fastapi import APIRouter

router = APIRouter()

@router.post("/validate")
async def validate_content(content: str):
  return {"is_valid": True, "content": content}
