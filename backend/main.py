from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from PIL import Image
from .captioner import ImageCaptioner
import io
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
INDEX_PATH = BASE_DIR / "index.html"

# Load captioner once at startup to avoid reloading the model per request.
captioner = ImageCaptioner()

@app.get("/")
async def read_root():
    return HTMLResponse(content=INDEX_PATH.read_text(), status_code=200)

@app.post("/caption/")
async def create_caption(file: UploadFile = File(...)):
    # Read image as binary
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    
    # Generate caption
    caption = captioner.caption(image)

    return {"caption": caption}
