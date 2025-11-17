import uvicorn
from app.core.config import settings

def start():
  workers = 1
  if settings.APP_ENV == "production":
    workers = settings.APP_WORKERS

  uvicorn.run(
    "app.main:app",
    port=settings.PORT,
    reload=settings.DEBUG,
    workers=workers
  )

if __name__ == "__main__":
  start()
