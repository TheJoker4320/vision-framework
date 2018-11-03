import cv2
from IFilter import IFilter


class BiggestAreaFilter(IFilter):
    """
    goes over all the contours and returrn the one with the biggest area
    returned as a list with one element
    """

    def filter(self, contours):
        return [max(contours, key=cv2.contourArea)]
