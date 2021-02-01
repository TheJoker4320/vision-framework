from extractors.extractor import Extractor
import cv2
import numpy


class CirclesExtractor(Extractor):
    """
    Extracts all the contours that are circular
    """

    dp: float
    minimum_distance: float

    def __init__(self, dp: float, minimum_distance: float):
        """
        :param dp: The inverse ratio of the accumulator resolution to the image resolution.
                   Essentially, the larger the dp gets, the smaller the accumulator array gets.
        :type dp: float

        :param minimum_distance: The minimum distance between the center (x, y) coordinates of detected circles.
                       If the distance is too small, multiple circles in the same neighborhood as the original may be
                      (falsely) detected. If the distance is too large, then some circles may not be detected at all.
        :type minimum_distance: float
        """
        self.dp = dp
        self.minimum_distance = minimum_distance

    def extract(self, frame: numpy.ndarray) -> [numpy.ndarray]:
        circles = cv2.HoughCircles(frame, cv2.HOUGH_GRADIENT, self.dp, self.minimum_distance)
        if circles is None:
            return []
        circles = numpy.round(circles[0, :]).astype("int")
        return [CirclesExtractor.__create_bounding_contour(circle) for circle in circles if circle[2]]

    @staticmethod
    def __create_bounding_contour(circle: numpy.ndarray) -> numpy.ndarray:
        """
        :param circle: A circle represented as (center_x, center_y, radius)
        :type circle: numpy array

        :return: A rectangle contour which bounds the circular rectangle
        :rtype: numpy array
        """
        center_x, center_y, radius = circle
        # print(center_x, center_y, radius)
        left_up_point = numpy.array([center_x - radius, center_y - radius])
        right_up_point = numpy.array([center_x + radius, center_y - radius])
        right_down_point = numpy.array([center_x + radius, center_y + radius])
        left_down_point = numpy.array([center_x - radius, center_y + radius])

        return numpy.array([left_up_point, right_up_point, right_down_point, left_down_point])
