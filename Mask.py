from IModifier import IModifier
import cv2


class Mask(IModifier):

    def __init__(self, mask):
        self.mask = mask

    def modify(self, frame):
        return cv2.bitwise_and(frame, frame, mask=self.mask)
