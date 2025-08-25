import numpy as np

def track_pixel_motion(frames, pixel=(100, 100)):
    if frames.ndim == 4:  # (num_frames, h, w, c)
        num_frames, h, w, c = frames.shape
        # Convert to grayscale intensity by averaging channels
        gray_frames = np.mean(frames, axis=-1)
    elif frames.ndim == 3:  # (num_frames, h, w)
        num_frames, h, w = frames.shape
        gray_frames = frames
    else:
        raise ValueError("Unsupported frame shape: {}".format(frames.shape))

    x, y = pixel
    signal = gray_frames[:, y, x]  

    return signal
