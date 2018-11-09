from IModifier import IModifier
import cv2


class ColorThreshold(IModifier):
    """
    Doing threshold color using HSV
    """
    def __init__(self, low_hsv, high_hsv):
        self.low_hsv = low_hsv
        self.high_hsv = high_hsv

    def modify(self, pic):
        hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
        hsv = cv2.inRange(hsv, self.low_hsv, self.high_hsv)
        return hsv
