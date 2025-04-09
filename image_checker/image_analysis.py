import os
import numpy as np
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
import logging

logger = logging.getLogger(__name__)

class ImageAnalyzer:
    def __init__(self):
        self.processor = None
        self.model = None

    def analyze_image(self, image_path):
        try:
            if self.processor is None or self.model is None:
                self.processor = AutoImageProcessor.from_pretrained("Falconsai/nsfw_image_detection")
                self.model = AutoModelForImageClassification.from_pretrained("Falconsai/nsfw_image_detection")
            image = Image.open(image_path)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            inputs = self.processor(images=image, return_tensors="pt")
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                probs = torch.nn.functional.softmax(logits, dim=-1)
            nsfw_prob = probs[0, 1].item()
            predicted_class = torch.argmax(probs, dim=1).item()
            class_label = "NSFW" if predicted_class == 1 else "Safe"
            if nsfw_prob > 0.7:
                return f"WARNING: This image contains NSFW content (Probability: {nsfw_prob:.2%})"
            elif nsfw_prob > 0.3:
                return f"CAUTION: This image might contain sensitive content (Probability: {nsfw_prob:.2%})"
            else:
                return f"This image appears to be safe for social media (Probability: {nsfw_prob:.2%})"
        except Exception as e:
            logger.error(f"Error in analyze_image: {str(e)}")
            return f"Error analyzing image: {str(e)}"
