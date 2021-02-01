from modifiers.modifier import Modifier
import cv2
import numpy


class ColorThreshold(Modifier):
    """
    Applies color threshold using HSV
    Can perform mask, via bitwise AND operation, between the original frame and the HSV
    Returns the modified frame
    """
    low_hsv: numpy.ndarray
    high_hsv: numpy.ndarray
    do_mask: bool

    def __init__(self, low_h: float, low_s: float, low_v: float, high_h: float, high_s: float, high_v: float,
                 do_mask: bool):
        """
        :param low_h: The lower limit of the Hue range
        :type low_h: float

        :param low_s: The lower limit of the Saturation range
        :type low_s: float

        :param low_v: The lower limit of the Value range
        :type low_v: float

        :param high_h: The higher limit of the Hue range
        :type high_h: float

        :param high_s: The higher limit of the Saturation range
        :type high_s: float

        :param high_v: The higher limit of the value range
        :type high_v: float

        :param do_mask: Flag for performing mask
        :type do_mask: boolean
        """

        # Create a lower boundary array
        self.low_hsv = numpy.array([low_h, low_s, low_v])
        # Create an upper boundary array
        self.high_hsv = numpy.array([high_h, high_s, high_v])

        self.do_mask = do_mask

    def modify(self, frame: numpy.ndarray) -> numpy.ndarray:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.low_hsv, self.high_hsv)
        if self.do_mask:
            mask = cv2.bitwise_and(frame, frame, mask=mask)

        return mask
