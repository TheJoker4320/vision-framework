from IModifier import IModifier
import cv2

"""blurs the image using kernel"""


class Blur(IModifier):

    def __init__(self, kernel):
        self.kernel = kernel

    def modify(self, pic):
        return cv2.GaussianBlur(pic, self.kernel, 0)
