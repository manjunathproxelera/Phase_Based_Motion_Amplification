import scipy.signal as signal
import numpy as np

def temporal_bandpass(frames, low, high, fps):
    try:
        if frames is None or len(frames) == 0:
            raise ValueError("Frames are empty.")

        nyquist = 0.5 * fps
        if high >= nyquist:
            raise ValueError(
                f"High cutoff {high} Hz must be less than Nyquist {nyquist:.2f} Hz"
            )

        # Ensure frames are 2D: (time, features)
        frames = np.asarray(frames)
        if frames.ndim == 3:  
            # flatten HxW → channels
            frames = frames.reshape(frames.shape[0], -1)

        if frames.shape[0] <= 50:
            raise ValueError(
                f"Not enough frames ({frames.shape[0]}) for padlen=50"
            )

        b, a = signal.butter(4, [low/nyquist, high/nyquist], btype="band")
        filtered = signal.filtfilt(b, a, frames, axis=0, padlen=50)
        return filtered

    except Exception as e:
        print(f"[Error in temporal_bandpass] {e}")
        return None
