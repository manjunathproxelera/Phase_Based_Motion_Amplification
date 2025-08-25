import cv2
import os
import numpy as np

def load_offline_video(path, gray=False, normalize=False, show=True):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Video file not found: {path}")

    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video: {path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if normalize:
            frame = frame.astype("float32") / 255.0

        frames.append(frame)

    cap.release()
    cv2.destroyAllWindows()
    frames = np.array(frames)
    print(f"Loaded {len(frames)} frames from {path}")
    return path,frames, fps, width, height, total


if __name__ == "__main__":
    # Example standalone usage
    video_file = "input/camera.mp4"
    path,frames, fps, w, h, total = load_offline_video(video_file, gray=True, normalize=True)
    print("Video shape:", frames.shape)
