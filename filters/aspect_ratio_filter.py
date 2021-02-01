from filters.filter import Filter
from numpy import ndarray
import cv2
import calculation_utils


class AspectRatioFilter(Filter):
    """
    Filters the contours by minimum and maximum values of the aspect ratio
    The aspect ratio defined as the ratio between the height and width
    Height defined as the longer between the two side's length
    """

    min_ratio: float
    max_ratio: float

    def __init__(self, min_ratio: float, max_ratio: float):
        """
        :param min_ratio: The minimum aspect ratio of the contour to filter
        :type min_ratio: float

        :param max_ratio: The maximum aspect ratio of the contour to filter
        :type max_ratio: float
        """
        self.min_ratio = min_ratio
        self.max_ratio = max_ratio

    def __in_aspect_ratio(self, contour: ndarray) -> bool:
        """
        Checks if the contour aspect ratio is in the desired range

        :param contour: A contour to check
        :type contour: ndarray

        :return: True or False
        :rtype: boolean
        """

        rectangle = cv2.minAreaRect(contour)
        p0, p1, p2, p3 = cv2.boxPoints(rectangle)  # the rectangle's points

        side1 = calculation_utils.distance(p0, p1)
        side2 = calculation_utils.distance(p1, p2)

        aspect_ratio = float(max(side1, side2)) / min(side1, side2)

        if self.min_ratio <= aspect_ratio <= self.max_ratio:
            return True
        return False

    def filter(self, contours: [ndarray]) -> [ndarray]:
        return [contour for contour in contours if self.__in_aspect_ratio(contour)]
