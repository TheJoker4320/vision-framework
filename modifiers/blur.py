from modifier import Modifier
import cv2


class Blur(Modifier):
    """Blurs the image using a kernel."""

    def __init__(self, kernel):
        """
        :param kernel: bluring kernel
        :type kernel: tuple
        """
        self.kernel = tuple(kernel)

    def modify(self, pic):
        return cv2.GaussianBlur(pic, self.kernel, 0)
