from filters.filter import Filter
from numpy import ndarray
import cv2


class BiggestAreaFilter(Filter):
    """
    Goes over all the contours and returns the one with the biggest area
    Returned as a list with one element
    """

    def filter(self, contours: [ndarray]) -> [ndarray]:
        return [max(contours, key=cv2.contourArea)] if contours != [] else contours
