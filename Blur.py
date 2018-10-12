from IModifier import IModifier
import cv2


class Blur(IModifier):

    def __init__(self, frame, blur_kernel):
        self.frame = frame
        self.blur_kernel = blur_kernel

    def modify(self, frame):
        frame = cv2.GaussianBlur(self.frame, self.blur_kernel, 0)
        return frame
