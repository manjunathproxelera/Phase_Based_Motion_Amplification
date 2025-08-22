import numpy as np
import matplotlib.pyplot as plt

def save_frequency_spectrum(frames, fps, save_path_spectrum, save_path_phase, pixel_coords=(100,100)):
    # Extract temporal signal from a single pixel
    signal = frames[:, pixel_coords[0], pixel_coords[1]]

    # FFT
    freqs = np.fft.rfftfreq(len(signal), 1/fps)
    spectrum = np.abs(np.fft.rfft(signal))
    phase = np.angle(np.fft.rfft(signal))

    # --- Magnitude Spectrum ---
    plt.figure(figsize=(8,4))
    plt.plot(freqs, spectrum, label="Magnitude")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.title(f"Frequency Spectrum at Pixel {pixel_coords}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path_spectrum, dpi=150)
    plt.close()

    # --- Phase Spectrum ---
    plt.figure(figsize=(8,4))
    plt.plot(freqs, phase, label="Phase", color="orange")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (radians)")
    plt.title(f"Phase Spectrum at Pixel {pixel_coords}")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path_phase, dpi=150)
    plt.close()

    print(f"[INFO] Frequency spectrum saved to {save_path_spectrum}")
    print(f"[INFO] Phase spectrum saved to {save_path_phase}")
