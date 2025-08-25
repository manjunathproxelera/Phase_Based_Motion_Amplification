from src.phase_decomposition import build_pyramid
from src.temporal_filter import temporal_bandpass
from src.amplifier import amplify_motion
from src.reconstructor import save_video
from src.frequency_analysis import save_frequency_spectrum
from src.detect_frequency import detect_motion_frequency_range
import os
import sys
import numpy as np
from src.video_loader.live_video import record_live_stream
from src.video_loader.offline_video import load_offline_video


def main():
    try:
        print("Starting Motion Amplification Pipeline...")

        # --- Step 1: Record live video or use file ---
        video_path = 'input/babysleeping.mp4'  # change to 0 to record live from webcam

        if video_path == 0:
            # Record live video in color
            video_path, frame_count, h, w, fps = record_live_stream(gray=False)
            print(f"Recorded {frame_count} frames, resolution: {w}x{h}, FPS: {fps}")

        # --- Step 2: Load video frames (grayscale for processing) ---
        video_path, frames, fps, w, h, total_frames = load_offline_video(
            video_path, gray=True, normalize=True
        )

        if frames is None or len(frames) == 0:
            raise RuntimeError(f"No frames loaded from video: {video_path}")

        print(f"Loaded {len(frames)} frames, FPS: {fps}, Width: {w}, Height: {h}")
        print(f"Frames shape: {frames.shape}")

        # --- Step 3: Detect motion frequency ---
        low_freq, high_freq, peak_freq, xf, yf = detect_motion_frequency_range(
            video_path, pixel_coords=(100, 100)
        )
        print(f"Detected dominant frequency: {peak_freq:.2f} Hz")
        print(f"Frequency band: {low_freq:.2f} - {high_freq:.2f} Hz")

        # --- Step 4: Build phase pyramid on first frame ---
        print("Building pyramid on first frame...")
        try:
            _ = build_pyramid(frames[0])  # frames[0] must be 2D
            print("Phase pyramid built successfully.")
        except Exception as e:
            raise RuntimeError(f"Error in phase decomposition: {e}")

        # --- Step 5: Frequency spectrum analysis ---
        spectrum_path = "output/motion_spectrum.png"
        phase_path = "output/motion_phase.png"
        print("Analyzing frequency spectrum...")
        save_frequency_spectrum(frames, fps, spectrum_path, phase_path, pixel_coords=(100, 100))
        print(f"Frequency spectrum saved at: {spectrum_path}")

        # --- Step 6: Temporal filtering ---
        print(f"Applying temporal bandpass filter ({low_freq:.2f}-{high_freq:.2f} Hz)...")
        filtered_frames = temporal_bandpass(frames, low_freq, high_freq, fps)
        if filtered_frames.shape != frames.shape:
            filtered_frames = filtered_frames.reshape(frames.shape)
        print("Temporal filtering complete.")

        # --- Step 7: Motion amplification ---
        amplification_factor = 20
        print(f"Amplifying motion (factor={amplification_factor})...")
        amplified_frames = amplify_motion(frames, filtered_frames, amplification_factor)
        print("Motion amplification done.")

        # --- Step 8: Save output video ---
        output_path = "output/amplified_motion.mp4"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        save_video(amplified_frames, output_path, fps)
        print(f"Done! Output saved to {output_path}")

    except Exception as e:
        print("Pipeline Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
