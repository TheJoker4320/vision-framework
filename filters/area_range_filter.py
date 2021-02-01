from filters.filter import Filter
from numpy import ndarray
import cv2


class AreaRangeFilter(Filter):
    """
    Filters the contours by minimum and maximum values of the area
    The area is defined by the contour area
    """

    min_area: float
    max_area: float

    def __init__(self, min_area: float, max_area: float):
        """
        :param min_area: The minimum area of the contour to filter
        :type min_area: float

        :param max_area: The maximum area of the contour to filter
        :type max_area: float
        """
        self.min_area = min_area
        self.max_area = max_area

    def __check_area_range(self, contour: ndarray) -> bool:
        """
        Checks if the contour area is in the desired range

        :param contour: A contour to check
        :type contour: ndarray

        :return: True or False
        :rtype: boolean
        """
        area = cv2.contourArea(contour)
        return self.min_area <= area <= self.max_area

    def filter(self, contours: [ndarray]) -> [ndarray]:
        return list(filter(self.__check_area_range, contours))
