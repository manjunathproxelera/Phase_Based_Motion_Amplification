import cv2
import numpy as np
import pyrtools as pt
from scipy.signal import butter, filtfilt
import imageio

# --- Load video ---
video_path = "billDaughter.wmv"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    raise IOError(f"Cannot open video: {video_path}")

frames = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray.astype(np.float32) / 255.0)  # normalize
cap.release()

frames = np.array(frames)
print(f"Loaded {len(frames)} frames, shape: {frames.shape}")

# --- Temporal bandpass filter ---
def butter_bandpass(low, high, fs, order=3):
    nyq = 0.5 * fs
    low /= nyq
    high /= nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

fps = 30
low_freq, high_freq = 0.4, 1.0
b, a = butter_bandpass(low_freq, high_freq, fps)

filtered_frames = filtfilt(b, a, frames, axis=0)

# --- Amplify motion ---
amplification_factor = 20
amplified_frames = frames + amplification_factor * filtered_frames

# Clip values to [0,1] to avoid overflow
amplified_frames = np.clip(amplified_frames, 0, 1)

# --- Save output video ---
output_path = "amplified_motion.mp4"

# Convert each frame back to RGB for saving
rgb_frames = [(np.stack([f, f, f], axis=-1) * 255).astype(np.uint8) for f in amplified_frames]

imageio.mimsave(output_path, rgb_frames, fps=fps)
print(f" Output saved to {output_path}")

