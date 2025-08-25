import cv2
import os
import numpy as np

def load_video(path=0, gray=False, normalize=False):
    try:
        # If path is 0 (webcam), skip os.path.exists check
        if isinstance(path, str) and not os.path.exists(path):
            raise FileNotFoundError(f"Video file not found: {path}")

        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            raise IOError(f"Cannot open video source: {path}")

        fps = cap.get(cv2.CAP_PROP_FPS)
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # total = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Show webcam/video feed
            cv2.imshow("Webcam Feed", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            if gray:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            if normalize:
                frame = frame.astype("float32") / 255.0
            frames.append(frame)

        frames = np.array(frames)
        cap.release()
        cv2.destroyAllWindows()

        return frames, fps, w,h

    except Exception as e:
        print(f"Error while loading video: {e}")
        return None, None, None, None, None
