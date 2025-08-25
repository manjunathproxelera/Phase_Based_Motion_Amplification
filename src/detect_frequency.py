import cv2
import numpy as np
from scipy.fft import fft, fftfreq

def detect_motion_frequency_range(video_path, pixel_coords=None, band_margin=0.5):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

    # default to center pixel if not given
    if pixel_coords is None:
        pixel_coords = (h // 2, w // 2)

    # collect intensity signal over time
    signal = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        y, x = pixel_coords
        signal.append(gray[y, x])


    cap.release()
    signal = np.array(signal)

    # FFT
    N = len(signal)
    yf = np.abs(fft(signal - np.mean(signal)))  # remove DC
    xf = fftfreq(N, 1 / fps)

    # only positive freqs
    pos_mask = xf > 0
    xf = xf[pos_mask]
    yf = yf[pos_mask]

    # find dominant frequency
    peak_idx = np.argmax(yf)
    peak_freq = xf[peak_idx]

    # define band around peak
    low = max(0.1, peak_freq - band_margin)
    high = peak_freq + band_margin

    return low, high, peak_freq, xf, yf
