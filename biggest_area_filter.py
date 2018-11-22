import cv2
from filter import Filter


class BiggestAreaFilter(Filter):

    """
    Goes over all the contours and returns the one with the biggest area
    returned as a list with one element
    """

    def filter(self, contours):
        return [max(contours, key=cv2.contourArea)]
