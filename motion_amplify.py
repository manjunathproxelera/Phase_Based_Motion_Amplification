from src.video_loader import load_video
from src.phase_decomposition import build_pyramid
from src.temporal_filter import temporal_bandpass
from src.amplifier import amplify_motion
from src.reconstructor import save_video
from src.frequency_analysis import save_frequency_spectrum
from src.detect_frequency import detect_motion_frequency_range
import os
import sys

video_path =0 # Change to 0 for webcam  
output_path = "output/amplified_motion.mp4"
amplification_factor = 20
spectrum_path = "output/motion_spectrum.png"
phase_path = "output/motion_phase.png"

def main():
    try:
        print("Starting Motion Amplification Pipeline...")
        print("Loading video...")
        frames, fps, w, h = load_video(video_path,gray=True, normalize=True)
        
        if frames is not None:
            print(f"Loaded {len(frames)} frames")
            print(f"FPS: {fps}, Width: {w}, Height: {h}")


        print(f"Loaded {len(frames)} frames, shape: {frames.shape}")
        # low_freq,high_freq,peak_freq,xf,yf = detect_motion_frequency_range(path, pixel_coords=(100,100))
        # print(f"Detected dominant frequency: {peak_freq:.2f} Hz")
        # print(f"Frequency band: {low_freq:.2f} - {high_freq:.2f} Hz")
        # try:
        #     _ = build_pyramid(frames[0])
        #     print("Phase pyramid built successfully.")
        # except Exception as e:
        #     raise RuntimeError(f"Error in phase decomposition: {e}")

        # print("Analyzing frequency spectrum...")
        # save_frequency_spectrum(
        #     frames, fps, spectrum_path, phase_path, pixel_coords=(100, 100)
        # )
        # print(f"Frequency spectrum saved at: {spectrum_path}")

        # print(f"Applying temporal bandpass filter ({low_freq}-{high_freq} Hz)...")
        # filtered_frames = temporal_bandpass(frames, low_freq, high_freq, fps)
        # print("Temporal filtering complete.")

        # print(f"Amplifying motion (factor={amplification_factor})...")
        # amplified_frames = amplify_motion(frames, filtered_frames, amplification_factor)
        # print("Motion amplification done.")

        # print("Saving amplified video...")
        # os.makedirs(os.path.dirname(output_path), exist_ok=True)
        # save_video(amplified_frames, output_path, fps)
        # print(f"Done! Output saved to {output_path}")

    except Exception as e:
        print("Pipeline Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
