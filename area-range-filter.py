from filter import filter
import cv2

"""Filters the contours according to the area range"""


class AreaRangeFilter(filter):

    """
    Filters the contours by minimum and maximum values of the area.
    The area is defined by tho contour area.
    """

    def __init__(self, min_area, max_area):
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
        if self.min_area <= area <= self.max_area:
            return True
        return False

    def filter(self, contours):
        return [contour for contour in contours if self.__check_area_range(contour)]
