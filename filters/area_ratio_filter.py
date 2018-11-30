import cv2
from filter import Filter
import utils


class AreaRatioFilter(Filter):
    """
    Filters the contours by minimum and maximum values of the area ratio.
    The area ratio is defined as the ratio between the rectangle area and contour area.
    """

    def __init__(self, min_area_ratio, max_area_ratio):
        self.min_area_ratio = min_area_ratio
        self.max_area_ratio = max_area_ratio

    def __check_area_ratio(self, contour):
        """
        :param contour: a contour to check
        :type contour: contour
        :return: is the contour in the desired range
        :rtype: boolean
        """

        rect = cv2.minAreaRect(contour)
        point1, point2, point3, _ = cv2.boxPoints(rect)
        rect_height = utils.distance(point1, point2)
        rect_width = utils.distance(point2, point3)
        rect_area = rect_width * rect_height
        cnt_area = cv2.contourArea(contour)  # The contour area

        if rect_area == 0:
            return False
        fullness_ratio = cnt_area / float(rect_area)

        return self.max_area_ratio >= fullness_ratio >= self.min_area_ratio

    def filter(self, contours):
        return [contour for contour in contours if self.__check_area_ratio(contour)]
