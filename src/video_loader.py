import cv2
import numpy as np

def load_video(video_path, gray=True):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(frame)
    
    cap.release()
    return np.array(frames, dtype=np.float32)
