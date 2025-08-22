import pyrtools as pt

def build_pyramid(frame, height=4, order=3):
    pyr = pt.pyramids.SteerablePyramidSpace(frame, height=height, order=order)
    return pyr.pyr_coeffs
