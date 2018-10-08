from IModifier import IModifier
import cv2


class MorphOpen(IModifier):

    def __init__(self, frame, morph_kernel):
        self.frame = frame
        self.morph_kernel = morph_kernel

    def modify(self, frame):
        frame = cv2.morphologyEx(self.frame, cv2.MORPH_CLOSE, self.morph_kernel)
        return frame