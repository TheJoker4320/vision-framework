from IModifier import IModifier
import cv2


class MaskModifier(IModifier):
    """
    Masks the mask image with the original image
    using bitwise and
    """
    def __init__(self, mask):
        self.mask = mask

    def modify(self, frame):
        return cv2.bitwise_and(frame, frame, mask=self.mask)
