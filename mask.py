from IModifier import IModifier
import cv2

""" Masks the mask image with the original image by using bitwise and """


class MaskModifier(IModifier):
    def __init__(self, mask):
        self.mask = mask

    def modify(self, frame):
        return cv2.bitwise_and(frame, frame, mask=self.mask)
