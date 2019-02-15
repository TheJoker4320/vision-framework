from extractor import Extractor
import cv2
import numpy


class CirclesExtractor(Extractor):
    """
    Extracts all the contours that are circular
    """

    def __init__(self, dp, minimum_distance):
        self.dp = dp
        self.minimum_distance = minimum_distance

    def extract(self, image):
        circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, self.dp, self.minimum_distance)
        if circles is None:
            return []
        circles = numpy.round(circles[0, :]).astype("int")
        return [CirclesExtractor.__create_bounding_contour(circle) for circle in circles if circle[2]]

    @staticmethod
    def __create_bounding_contour(circle):
        """
        :param circle: A circle represented as (center_x, center_y, radius)
        :type circle: numpy array
        :return: A rectangle contour which bounds the circular rectangle
        :rtype: numpy array
        """
        center_x, center_y, radius = circle
        print center_x, center_y, radius
        left_up_point = numpy.array([center_x - radius, center_y - radius])
        right_up_point = numpy.array([center_x + radius, center_y - radius])
        right_down_point = numpy.array([center_x + radius, center_y + radius])
        left_down_point = numpy.array([center_x - radius, center_y + radius])

        return numpy.array([left_up_point, right_up_point, right_down_point, left_down_point])
