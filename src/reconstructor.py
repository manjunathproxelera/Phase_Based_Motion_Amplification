import imageio
import numpy as np

def save_video(frames, output_path, fps=30):
    imageio.mimsave(output_path, (frames * 255).astype(np.uint8), fps=fps)
    print(f"Output saved to {output_path}")
