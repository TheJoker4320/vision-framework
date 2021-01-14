from modifiers.modifier import Modifier
import cv2
import numpy


class Morph(Modifier):
    """
    Applies either open, close, both open and close or none of them on a frame
    Returns the modified frame
    """

    def __init__(self, morph_open, morph_close):
        """
        :param morph_open: An array for the close method
        :type morph_open: numpy array
        :param morph_close:  A numpy array for the open method
        :type morph_close: numpy array
        """
        self.morph_open = numpy.ones(morph_open)
        self.morph_close = numpy.ones(morph_close)

    def modify(self, frame):

        modified_frame = frame
        empty = numpy.ones((0, 0))

        if self.morph_open != empty:
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, self.morph_open)

        if self.morph_close != empty:
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, self.morph_close)

        return modified_frame
