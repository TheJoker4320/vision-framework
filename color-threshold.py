from modifier import Modifier
import cv2


class ColorThreshold(Modifier):
    
    """Setting color threshold via the HSV values"""

    def __init__(self, low_hsv, high_hsv):
        """
        :param low_hsv: the lower limit of the HSV range
        :type low_hsv: list
        :param high_hsv: the higher limit of the HSV range
        :type high_hsv: list
        """
        self.low_hsv = low_hsv
        self.high_hsv = high_hsv

    def modify(self, pic):
        hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
        hsv = cv2.inRange(hsv, self.low_hsv, self.high_hsv)
        return hsv
