from modifier import Modifier
import cv2
import numpy


class ColorThreshold(Modifier):
    """
    Applies color threshold using HSV
    Can perform mask, via bitwise AND operation, between the original frame and the HSV
    Returns the modified frame
    """

    def __init__(self, low_h, low_s, low_v, high_h, high_s, high_v, do_mask):
        """
        :param low_hsv: the lower limit of the HSV range
        :type low_hsv:
        :param high_hsv: The higher limit of the HSV range
        :type high_hsv:
        :param do_mask: Flag for performing mask
        :type do_mask: boolean
        """

        self.low_hsv = numpy.array([low_h, low_s, low_v])
        self.high_hsv = numpy.array([high_h, high_s, high_v])
        self.do_mask = do_mask

    def modify(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.low_hsv, self.high_hsv)
        if self.do_mask:
            mask = cv2.bitwise_and(frame, frame, mask=mask)

        return mask
