from filter import Filter
import cv2


class AreaRangeFilter(Filter):
    """
    Filters the contours by minimum and maximum values of the area.
    The area is defined by the contour area.
    """

    def __init__(self, min_area, max_area):
        """

        :param min_area: The minimum of the contour to filter
        :param max_area: The maximum are of the contour to filter
        """
        self.min_area = min_area
        self.max_area = max_area

    def __check_area_range(self, contour):
        """
        :param contour: a contour to check
        :type contour: contour
        :return: is the contour in the desired range
        :rtype: boolean
        """
        area = cv2.contourArea(contour)
        return self.min_area <= area <= self.max_area

    def filter(self, contours):
        return filter(self.__check_area_range, contours)
