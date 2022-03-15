from modifiers.modifier import Modifier
import cv2


class Blur(Modifier):
    """
    Blurs the image using a blur kernel
    Returns the modified frame
    """

    def __init__(self, kernel):
        """
        :param kernel: The blur kernel
        :type kernel: tuple
        """
        self.kernel = tuple(kernel)

    def modify(self, frame):
        return cv2.GaussianBlur(frame, self.kernel, 0)
