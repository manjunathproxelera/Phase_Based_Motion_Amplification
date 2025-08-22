import scipy.signal as signal
import numpy as np

def temporal_bandpass(frames, fps, freq_range=(0.4, 3)):
    """Apply temporal bandpass filter on frames."""
    nyquist = 0.5 * fps
    b, a = signal.butter(4, [freq_range[0]/nyquist, freq_range[1]/nyquist], btype="band")
    
    filtered = signal.filtfilt(b, a, frames, axis=0, padlen=50)
    return filtered
