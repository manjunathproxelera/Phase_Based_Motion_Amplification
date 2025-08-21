import numpy as np
import cv2

def decompose_frames(frames):
    return frames - np.mean(frames, axis=0)  # Simple normalization
