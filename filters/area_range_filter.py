from filters.filter import Filter
import cv2


class AreaRangeFilter(Filter):
    """
    Filters the contours by minimum and maximum values of the area
    The area is defined by the contour area
    """

    def __init__(self, min_area, max_area):
        """
        :param min_area: The minimum area of the contour to filter
        :param max_area: The maximum area of the contour to filter
        """
        self.min_area = min_area
        self.max_area = max_area

    def __check_area_range(self, contour):
        """
        Checks if the contour area is in the desired range
        :param contour: A contour to check
        :type contour: contour
        :return: True or False
        :rtype: boolean
        """
        area = cv2.contourArea(contour)
        return self.min_area <= area <= self.max_area

    def filter(self, contours):
        return list(filter(self.__check_area_range, contours))
