from modifiers.modifier import Modifier
from numpy import ndarray
import cv2


class Blur(Modifier):
    """
    Blurs the image using a blur kernel
    Returns the modified frame
    """

    kernel: tuple

    def __init__(self, kernel: tuple):
        """
        :param kernel: The blur kernel
        :type kernel: tuple
        """
        self.kernel = tuple(kernel)

    def modify(self, frame: ndarray) -> ndarray:
        return cv2.GaussianBlur(frame, self.kernel, 0)
