try:
  import unzip_requirements
except ImportError:
  pass

from fastapi import FastAPI
from mangum import Mangum
from starlette.requests import Request
from app.api.api_v1.api import router as api_router
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = FastAPI()

@app.get("/")
def read_root(request: Request):
    logging.info("root url executed")
    return {"Hello": "World"}
    # return {"Hello": "World", "aws_event": request.scope["aws.event"]}

app.include_router(api_router, prefix="/api/v1")

handler = Mangum(
    app,
    lifespan="auto",
    log_level="info",
    api_gateway_base_path=None,
    text_mime_types=None
)