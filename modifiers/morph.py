from modifier import Modifier
import cv2
import numpy


class Morph(Modifier):
    """
    gets a frame and applies open or close or both open and close
    or none of them and returns the modified frame
    """

    def __init__(self, morph_open, morph_close):
        """

        :param morph_open: a numpy array for the close method
        :param morph_close:  a numpy array for the open method
        """
        self.morph_open = numpy.ones(morph_open)
        self.morph_close = numpy.ones(morph_close)

    def modify(self, frame):
        modified_frame = frame
        if self.morph_open != (0, 0):
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, self.morph_open)
        if self.morph_close != (0, 0):
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, self.morph_close)
        return modified_frame
