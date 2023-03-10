import argparse
from stable_diffusion_tf.stable_diffusion import StableDiffusion
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument(
    "--output",
    type=str,
    nargs="?",
    default="img2img-out.jpeg",
    help="the output image filename",
)

args = parser.parse_args()

generator = StableDiffusion(
    img_height=512,
    img_width=512,
    jit_compile=False,
)

img = generator.generate(
    args.prompt,
    negative_prompt=args.negative_prompt,
    num_steps=args.steps,
    unconditional_guidance_scale=7.5,
    temperature=1,
    batch_size=1,
    input_image=args.input,
    input_image_strength=0.8,
)
Image.fromarray(img[0]).save(args.output)
