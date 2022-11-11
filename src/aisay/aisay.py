from diffusers import StableDiffusionPipeline
from pathlib import Path

CUR_DIR = Path(__file__).absolute().parent



if __name__ == "__main__":
    print(CUR_DIR)
    pipe = StableDiffusionPipeline.from_pretrained(CUR_DIR / "stable-diffusion-v1-1")
    pipe = pipe.to("mps")

    # Recommended if your computer has < 64 GB of RAM
    pipe.enable_attention_slicing()

    prompt = "a photo of an astronaut riding a horse on mars"

    # First-time "warmup" pass (see explanation above)
    _ = pipe(prompt, num_inference_steps=1)

    # Results match those from the CPU device after the warmup pass.
    image = pipe(prompt).images[0]
    pass