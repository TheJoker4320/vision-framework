from IModifier import IModifier
import cv2


class Blur(IModifier):
    """
    blurs the image using kernel
    """

    def __init__(self, kernel):
        self.kernel = kernel

    def modify(self, pic):
        return cv2.GaussianBlur(pic, self.kernel, 0)
