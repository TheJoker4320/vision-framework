from modifier import Modifier
import cv2


class Blur(Modifier):
    """blurs the image using kernel"""

    def __init__(self, kernel):
        """

        :param kernel: bluring kernel
        :type kernel: tuple
        """
        self.kernel = kernel

    def modify(self, pic):
        return cv2.GaussianBlur(pic, self.kernel, 0)
