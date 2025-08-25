import cv2
import os
import numpy as np

def load_offline_video(path, gray=False, normalize=False, show=True):
    """
    Load video file for offline processing.

    Args:
        path: path to video file
        gray: convert frames to grayscale
        normalize: scale pixel values to [0,1]
        show: display frames while loading
    Returns:
        frames (np.array), fps, width, height, total_frames
    """
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

        if show:
            cv2.imshow("Video Feed", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        frames.append(frame)

    cap.release()
    cv2.destroyAllWindows()
    frames = np.array(frames)
    print(f"Loaded {len(frames)} frames from {path}")
    return frames, fps, width, height, total


if __name__ == "__main__":
    # Example standalone usage
    video_file = "input/camera.mp4"
    frames, fps, w, h, total = load_video(video_file, gray=True, normalize=True)
    print("Video shape:", frames.shape)
