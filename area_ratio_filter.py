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
        point1, point2, point3, point4 = cv2.boxPoints(rect)
        reg_height = utils.distance(point1, point2)
        reg_width = utils.distance(point3, point4)
        rect_area = reg_width * reg_height
        cnt_area = cv2.contourArea(contour)  # The contour area

        if self.max_area_ratio >= float(rect_area) / cnt_area >= self.min_area_ratio:
            return True
        return False

    def filter(self, contours):
        return [contour for contour in contours if self.__check_area_ratio(contour)]
