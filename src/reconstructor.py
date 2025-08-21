import cv2
import numpy as np

def save_video(frames, output_path, fps=30):
    h, w = frames[0].shape
    out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h), False)

    for frame in frames:
        frame = np.clip(frame, 0, 255).astype("uint8")
        out.write(frame)
    
    out.release()
