from src.video_loader import load_video
from src.phase_decomposition import decompose_frames
from src.temporal_filter import temporal_bandpass
from src.amplifier import amplify_motion
from src.reconstructor import save_video
from src.tracker import track_pixel_motion
from frequency_analysis import analyze_frequency

VIDEO_PATH = "input/camera.mp4"
OUTPUT_PATH = "output/amplified.mp4"
FPS = 30
AMPLIFICATION_FACTOR = 20
FREQ_RANGE = (0.5, 2.0)  # human breathing

def main():
    #Load Video
    frames = load_video(VIDEO_PATH, gray=True)
    print("Video Loaded:", frames.shape)

    #Phase Decomposition
    decomposed = decompose_frames(frames)

    #Temporal Filtering
    filtered = temporal_bandpass(decomposed, fps=FPS, freq_range=FREQ_RANGE)

    #Amplification
    amplified = amplify_motion(filtered, amplification_factor=AMPLIFICATION_FACTOR)

    #Reconstruct Video
    save_video(amplified, OUTPUT_PATH, fps=FPS)
    print("Amplified video saved at:", OUTPUT_PATH)

    #Motion Tracking (single pixel)
    signal = track_pixel_motion(frames)
    analyze_frequency(signal, fps=FPS, save_prefix="output/motion")

if __name__ == "__main__":
    main()
