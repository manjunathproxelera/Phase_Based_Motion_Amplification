import numpy as np

def track_pixel_motion(frames, point=None):
    num_frames, h, w = frames.shape
    if point is None:
        point = (h // 2, w // 2)
    return frames[:, point[0], point[1]]
