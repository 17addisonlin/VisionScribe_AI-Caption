from transformers import GitProcessor, GitForCausalLM
from PIL import Image
import torch

class ImageCaptioner:
    def __init__(self, device: str = None):
        # Set device to GPU if available, otherwise CPU
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"
        
        self.device = device
        
        # Initialize GIT model and processor
        self.processor = GitProcessor.from_pretrained("microsoft/git-large-coco")
        self.model = GitForCausalLM.from_pretrained("microsoft/git-large-coco").to(self.device)

    def caption(self, image: Image.Image, max_new_tokens: int = 30) -> str:
        # Process the image into the format expected by the model
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        # Generate caption using the model
        with torch.no_grad():
            output_ids = self.model.generate(**inputs, max_new_tokens=max_new_tokens)

        # Decode and return the generated caption
        caption = self.processor.batch_decode(output_ids, skip_special_tokens=True)[0]
        return caption


class SocialCaptioner:
    def __init__(self, base_captioner: ImageCaptioner | None = None, device: str = None):
        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.device = device
        self.base_captioner = base_captioner or ImageCaptioner(device=self.device)

    def caption(
        self,
        image: Image.Image,
        tone: str = "friendly",
        include_hashtags: bool = True,
        include_emojis: bool = True,
        max_new_tokens: int = 80,
    ) -> str:
        base_caption = self.base_captioner.caption(image)
        social_caption = self._apply_tone(base_caption, tone)

        if include_emojis:
            social_caption = f"{social_caption} {self._tone_emoji(tone)}"

        if include_hashtags:
            social_caption = f"{social_caption}\n{self._hashtags_from_caption(base_caption)}"

        return social_caption.strip()

    def _apply_tone(self, caption: str, tone: str) -> str:
        tone = tone.lower().strip()
        if tone == "playful":
            return f"{caption.capitalize()} Just vibing with the moment."
        if tone == "professional":
            return f"{caption.capitalize()} Captured with clarity and focus."
        if tone == "romantic":
            return f"{caption.capitalize()} A little moment to hold onto."
        if tone == "minimal":
            return caption.capitalize()
        if tone == "inspiring":
            return f"{caption.capitalize()} Proof that small moments can feel big."
        return f"{caption.capitalize()} Loving this scene."

    def _tone_emoji(self, tone: str) -> str:
        tone = tone.lower().strip()
        if tone == "playful":
            return "✨😄"
        if tone == "professional":
            return "📌✅"
        if tone == "romantic":
            return "💫❤️"
        if tone == "minimal":
            return "🤍"
        if tone == "inspiring":
            return "🌟🙌"
        return "✨📷"

    def _hashtags_from_caption(self, caption: str) -> str:
        words = [word.strip(".,!?:;").lower() for word in caption.split()]
        keywords = [word for word in words if len(word) > 3][:4]
        hashtags = " ".join(f"#{word}" for word in keywords) or "#photography #moment"
        return hashtags
