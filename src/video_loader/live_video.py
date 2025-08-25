import cv2
import os

def record_live_stream(input_folder="input", filename="camera.mp4", gray=False):
    """
    Record live webcam video until 'q' is pressed and save to input folder.

    Args:
        input_folder: folder to save recorded video
        filename: name of the saved video file
        gray: whether to convert frames to grayscale
    Returns:
        saved_path: full path of saved video
        frame_count: total frames recorded
        height: frame height
        width: frame width
    """
    if not os.path.exists(input_folder):
        os.makedirs(input_folder)

    save_path = os.path.join(input_folder, filename)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(save_path, fourcc, fps, (width, height), isColor=not gray)

    print("Recording live video. Press 'q' to stop.")
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        if gray:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Live Feed", frame)

        if gray:
            writer.write(cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR))
        else:
            writer.write(frame)

        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()
    print(f"Saved live video to: {save_path}, Total frames: {frame_count}")
    return save_path, frame_count, height, width


if __name__ == "__main__":
    # Run standalone
    saved_path, frame_count, h, w = record_live_video(gray=True)
    print("Video saved at:", saved_path)
    print(f"Frame count: {frame_count}, Height: {h}, Width: {w}")
