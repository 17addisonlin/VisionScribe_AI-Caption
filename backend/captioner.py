from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class ImageCaptioner:
    def __init__(self, device: str = None):
        # Set device to GPU if available, otherwise CPU
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.device = device
        
        # Initialize BLIP model and processor
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(self.device)

    def caption(self, image: Image.Image, max_new_tokens: int = 30) -> str:
        # Process the image into the format expected by the model
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        # Generate caption using the model
        with torch.no_grad():
            output_ids = self.model.generate(**inputs, max_new_tokens=max_new_tokens)

        # Decode and return the generated caption
        caption = self.processor.decode(output_ids[0], skip_special_tokens=True)
        return caption