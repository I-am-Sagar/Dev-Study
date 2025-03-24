from PIL import Image
from pathlib import Path
import os
import torch

def load_image(image_name, data_dir = 'src/data/images'):
    project_root = Path(__file__).parent.parent.parent

    image_path = project_root / data_dir / image_name

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    return Image.open(image_path)


def preprocess_image(image, clip_model):
    preprocess = clip_model.preprocess

    return preprocess(image).unsqueeze(0)