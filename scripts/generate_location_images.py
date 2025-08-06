from diffusers import StableDiffusionPipeline
import torch

model = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2")

locations = {
    "cape-town": "Table Mountain backdrop, sunny, professional business vibe",
    "stellenbosch": "Vineyard landscape, elegant winery style",
    "hermanus": "Ocean view, whales breaching, luxury aesthetic"
}

for town, prompt in locations.items():
    image = model(prompt).images[0]
    image.save(f"assets/{town}/cover.jpg")
