from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from PIL import Image
from captioner import ImageCaptioner, SocialCaptioner
import io
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
INDEX_PATH = BASE_DIR / "index.html"

# Load the base captioner at startup; defer the social model until needed.
captioner = ImageCaptioner()
social_captioner = None

def get_social_captioner() -> SocialCaptioner:
    global social_captioner
    if social_captioner is None:
        social_captioner = SocialCaptioner(base_captioner=captioner)
    return social_captioner

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

@app.post("/social-caption/")
async def create_social_caption(
    file: UploadFile = File(...),
    hashtags: bool = Form(True),
    emojis: bool = Form(True),
    tone: str = Form("friendly"),
):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    social_caption = get_social_captioner().caption(
        image=image,
        tone=tone,
        include_hashtags=hashtags,
        include_emojis=emojis,
    )

    return {"caption": social_caption}
