import numpy as np


def track_motion_red_selective(original_frames, amplified_motion, alpha=0.8, threshold=0.02):
    if len(original_frames.shape) != 4 or amplified_motion.shape != original_frames.shape[:3]:
        raise ValueError("Shape mismatch: frames and amplified_motion must match.")

    # Create mask for significant motion
    motion_mask = np.abs(amplified_motion) > threshold  # boolean mask

    # Prepare overlay: only red channel
    overlay_frames = np.copy(original_frames)
    
    # Apply red only where motion exists
    overlay_frames[motion_mask] = (
        (1 - alpha) * overlay_frames[motion_mask] + alpha * np.array([1.0, 0.0, 0.0])
    )

    return np.clip(overlay_frames, 0, 1)

