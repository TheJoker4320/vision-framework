from pipeline.pipeline_factory.PipelineFactory import modifier
from modifier import Modifier
import cv2


@modifier(name = "Color Threshold")
class ColorThreshold(Modifier):
    """
    Doing threshold color using HSV.
    Can perform mask, via bitwise and operation, between the original frame and the hsv
    """

    def __init__(self, low_hsv, high_hsv, do_mask):
        """

        :param low_hsv: the lower limit of the HSV range
        :type low_hsv:
        :param high_hsv: the higher limit of the HSV range
        :type high_hsv:
        :param do_mask: flag for performing mask
        :type do_mask: boolean
        """

        self.low_hsv = low_hsv
        self.high_hsv = high_hsv
        self.do_mask = do_mask

    def modify(self, pic):
        hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
        hsv = cv2.inRange(hsv, self.low_hsv, self.high_hsv)
        if self.do_mask:
            hsv = cv2.bitwise_and(pic, pic, mask=hsv)

        return hsv
