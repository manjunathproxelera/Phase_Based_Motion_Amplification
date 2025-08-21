import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def analyze_frequency(signal, fps, save_prefix="output/freq"):
    N = len(signal)
    T = 1.0 / fps
    yf = fft(signal - np.mean(signal))
    xf = fftfreq(N, T)[:N//2]

    # Magnitude spectrum
    plt.figure(figsize=(10,5))
    plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
    plt.title("Frequency Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.savefig(f"{save_prefix}_spectrum.png")

    # Phase spectrum
    plt.figure(figsize=(10,5))
    plt.plot(xf, np.angle(yf[:N//2]))
    plt.title("Phase Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Phase (radians)")
    plt.grid()
    plt.savefig(f"{save_prefix}_phase.png")
