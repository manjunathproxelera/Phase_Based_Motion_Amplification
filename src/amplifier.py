def amplify_motion(frames, filtered_frames, amplification_factor=20):
    return frames + amplification_factor * filtered_frames
