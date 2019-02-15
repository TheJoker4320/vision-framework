import cv2
from filter import Filter
import calculation_utils


class AreaRatioFilter(Filter):

    """
    Filters the contours by minimum and maximum values of the area ratio
    The area ratio is defined as the ratio between the rectangle area and contour area
    """

    def __init__(self, min_area_ratio, max_area_ratio):
        """
        :param min_area_ratio: The minimum area ratio of the contour to filter
        :param max_area_ratio: The maximum area ratio of the contour to filter
        """
        self.min_area_ratio = min_area_ratio
        self.max_area_ratio = max_area_ratio

    def __check_area_ratio(self, contour):
        """
        Checks if the contour area ratio is in the desired range
        :param contour: A contour to check
        :type contour: contour
        :return: True or False
        :rtype: boolean
        """

        rect = cv2.minAreaRect(contour)
        point1, point2, point3, _ = cv2.boxPoints(rect)
        rect_height = calculation_utils.distance(point1, point2)
        rect_width = calculation_utils.distance(point2, point3)
        rect_area = rect_width * rect_height
        cnt_area = cv2.contourArea(contour)

        if rect_area == 0:
            return False
        fullness_ratio = cnt_area / float(rect_area)

        return self.max_area_ratio >= fullness_ratio >= self.min_area_ratio

    def filter(self, contours):
        return [contour for contour in contours if self.__check_area_ratio(contour)]
