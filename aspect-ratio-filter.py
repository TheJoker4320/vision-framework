from filter import Filter
import cv2
import utils


class AspectRatioFilter(Filter):

    """
    Filters the contours by minimum and maximum values of the aspect ratio
    the aspect ratio defined as the ratio between the height and width
    height defined as the longer between the two side's length
    """

    def __init__(self, min_ratio, max_ratio):
        self.min_ratio = min_ratio
        self.max_ratio = max_ratio

    def __in_aspect_ratio(self, contour):

        """
        :param contour: a contour to check
        :type contour: contour
        :return: is the contour in the desired range
        :rtype: boolean
        """

        rectangle = cv2.minAreaRect(contour)
        p0, p1, p2, p3 = cv2.boxPoints(rectangle)  # the rectangle's points
        side1 = utils.distance(p0, p1)
        side2 = utils.distance(p1, p2)
        aspect_ratio = float(max(side1, side2)) / min(side1, side2)

        if self.min_ratio <= aspect_ratio <= self.max_ratio:
            return True
        return False

    def filter(self, contours):
        return [contour for contour in contours if self.__in_aspect_ratio(contour)]
