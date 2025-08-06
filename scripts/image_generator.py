from diffusers import StableDiffusionPipeline
import torch
import os

# scripts/image-generator.py (Updated for Silver)
model = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",  # Higher quality model
    torch_dtype=torch.float16,
    use_safetensors=True
)

# Generate 4K images for premium listings
image = model(
    "Professional business photo of Cape Town waterfront, 4K ultra HD",
    height=2160,
    width=3840
).images[0]

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
