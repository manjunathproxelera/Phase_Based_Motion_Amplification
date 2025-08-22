import cv2
import numpy as np

def load_video(video_path, gray=True, normalize=True):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video: {video_path}")

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if normalize:
            frame = frame.astype(np.float32) / 255.0
        frames.append(frame)

    cap.release()
    return np.array(frames)
