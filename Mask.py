from IModifier import IModifier
import cv2


class MaskModifier(IModifier):
    """
    masks the mask image with the original image by using bitwise and
    """
    def __init__(self, mask):
        self.mask = mask

    def modify(self, picure):
        return cv2.bitwise_and(frame, frame, mask=self.mask)
