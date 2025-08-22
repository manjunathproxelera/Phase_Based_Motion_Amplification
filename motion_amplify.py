from src.video_loader import load_video
from src.phase_decomposition import build_pyramid
from src.temporal_filter import apply_bandpass
from src.amplifier import amplify_motion
from src.reconstructor import save_video
from src.frequency_analysis import save_frequency_spectrum

# --- Parameters ---
video_path = "input/car_input_f50-650_50FPS-remove120.mp4"
output_path = "output/amplified_motion.mp4"
fps = 50
low_freq, high_freq = 50.0, 650.0
amplification_factor = 30
spectrum_path = "output/motion_spectrum.png"
phase_path = "output/motion_phase.png"

print("Loading video...")
frames = load_video(video_path, gray=True, normalize=True)
print(f"Loaded {len(frames)} frames, shape: {frames.shape}")

_ = build_pyramid(frames[0])

print("Analyzing frequency spectrum...")
save_frequency_spectrum(frames, fps, spectrum_path, phase_path, pixel_coords=(100,100))

print("Applying temporal bandpass filter...")
filtered_frames = apply_bandpass(frames, low_freq, high_freq, fps)

print("Amplifying motion...")
amplified_frames = amplify_motion(frames, filtered_frames, amplification_factor)

print("Saving video...")
save_video(amplified_frames, output_path, fps)

print(f"Done! Output saved to {output_path}")
