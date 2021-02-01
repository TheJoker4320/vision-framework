from filters.filter import Filter
from numpy import ndarray
import calculation_utils
import cv2


class AreaRatioFilter(Filter):

    """
    Filters the contours by minimum and maximum values of the area ratio
    The area ratio is defined as the ratio between the rectangle area and contour area
    """

    min_area_ratio: float
    max_area_ratio: float

    def __init__(self, min_area_ratio: float, max_area_ratio: float):
        """
        :param min_area_ratio: The minimum area ratio of the contour to filter
        :type min_area_ratio: float

        :param max_area_ratio: The maximum area ratio of the contour to filter
        :type max_area_ratio: float
        """
        self.min_area_ratio = min_area_ratio
        self.max_area_ratio = max_area_ratio

    def __check_area_ratio(self, contour: ndarray) -> bool:
        """
        Checks if the contour area ratio is in the desired range

        :param contour: A contour to check
        :type contour: ndarray

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

        return self.min_area_ratio <= fullness_ratio <= self.max_area_ratio

    def filter(self, contours: [ndarray]) -> [ndarray]:
        return [contour for contour in contours if self.__check_area_ratio(contour)]
