from filter import Filter
import cv2


class ShapeFilter(Filter):

    """
    Filters the contours by their approximate shape.
    checks the approximate shape according to epsilon value.
    as epsilon is bigger the filtering is more flexible.
    """

    def __init__(self, edges_count, epsilon):
        self.edges_count = edges_count
        self.epsilon = epsilon

    def __check_contour_shape(self, contour):
        """
        :param contour: a contour to check
        :type contour: contour
        :return: is the contour in the desired range
        :rtype: boolean
        """
        epsilon_arc = self.epsilon * cv2.arcLength(contour, True)
        approximate_polygon = cv2.approxPolyDP(contour, epsilon_arc, True)
        return len(approximate_polygon) == self.edges_count

    def filter(self, contours):
        return [contour for contour in contours if self.__check_contour_shape(contour)]
