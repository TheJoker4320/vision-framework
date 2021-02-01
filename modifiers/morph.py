from modifiers.modifier import Modifier
import cv2
import numpy


class Morph(Modifier):
    """
    Applies either open, close, both open and close or none of them on a frame
    Returns the modified frame
    """

    morph_open: numpy.ndarray
    morph_close: numpy.ndarray

    def __init__(self, morph_open: list, morph_close: list):
        """
        :param morph_open: The size of the kernel for the Opening method
        :type morph_open: list of 2 odd floats (or 0 to not use it)
        :param morph_close: The size of the kernel for the Closing method
        :type morph_close: list of 2 odd floats (or 0 to not use it)
        """
        self.morph_open = numpy.ones(morph_open)
        self.morph_close = numpy.ones(morph_close)

    def modify(self, frame: numpy.ndarray) -> numpy.ndarray:

        modified_frame = frame
        empty = numpy.ones((0, 0))

        if self.morph_open != empty:
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, self.morph_open)

        if self.morph_close != empty:
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, self.morph_close)

        return modified_frame
