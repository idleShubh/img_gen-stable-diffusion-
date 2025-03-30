# Stable Diffusion Image Generation (Mac)

This project uses **Stable Diffusion** to generate an image of *"a man playing guitar"* using the **Diffusers** library. It leverages **Metal Performance Shaders (MPS)** for Apple Silicon Macs.

<img width="1470" alt=" 30_March image_gen using diffusion " src="https://github.com/user-attachments/assets/1afe0496-b00a-4e14-b0fc-d2c336d79dfc" />

## Requirements

Ensure you have the following installed:

- Python 3.8+
- PyTorch with MPS support
- `diffusers` library
- `transformers` library
- `torchvision`
- `accelerate`

### Parameters:
- `num_inference_steps=50`: Controls the number of steps in the diffusion process (higher = better quality but slower).
- `guidance_scale=7.5`: Balances creativity and adherence to the prompt (higher = follows prompt more strictly).

## Notes
- This script is optimized for **Macs with Apple Silicon (M1/M2)** using `mps`.
- If using a different system, change `pipe.to("mps")` to `pipe.to("cuda")` (for NVIDIA GPUs) or `pipe.to("cpu")` (for CPUs).
- The first run may take longer as it downloads model weights.

## Example Output
After running the script, you should see an image of a person playing a guitar, saved as `guitar_player.png`.

## License
This project is open-source and uses the **Stable Diffusion** model under the Apache 2.0 License.

