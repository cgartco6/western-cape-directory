from diffusers import StableDiffusionPipeline
import torch
import os

model = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")

towns = {
    "cape-town": "Table Mountain with cityscape, professional business style",
    "stellenbosch": "Vineyard with mountains, elegant business atmosphere",
    "hermanus": "Whale watching from shore, luxury tourism style"
}

for town, prompt in towns.items():
    if not os.path.exists(f"public/assets/img/{town}"):
        os.makedirs(f"public/assets/img/{town}")
    
    image = model(prompt).images[0]
    image.save(f"public/assets/img/{town}/banner.jpg")
