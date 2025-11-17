from fastapi import APIRouter
from .socmed_content import router as socmed_content_router

router = APIRouter()

router.include_router(
  socmed_content_router, 
  prefix="/socmed-content", 
  tags=["Socmed-Content"],
)
