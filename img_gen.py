from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("mps")  # Use Metal Performance Shaders for Mac (Apple Silicon)

# Generate an image
prompt = "a man playing guitar"
image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]

# Save the image
image.save("guitar_player.png")

# Show the image
image.show()
