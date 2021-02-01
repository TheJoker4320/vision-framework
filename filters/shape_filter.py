from filters.filter import Filter
from numpy import ndarray
import cv2


class ShapeFilter(Filter):

    """
    Filters the contours by their approximate shape
    Checks the approximate shape according to epsilon value
    As epsilon is bigger the filtering is more flexible
    """

    edges_count: int
    epsilon: float

    def __init__(self, edges_count: int, epsilon: float):
        """
        :param edges_count: The number of edges
        :type edges_count: int

        :param epsilon: The value which is used to approximate the shape type
        :type epsilon: float
        """
        self.edges_count = edges_count
        self.epsilon = epsilon

    def __check_contour_shape(self, contour: ndarray) -> bool:
        """
        Checks if the contour shape matches to the epsilon value (shape)

        :param contour: A contour to check
        :type contour: ndarray

        :return: True or False
        :rtype: boolean
        """
        epsilon_arc = self.epsilon * cv2.arcLength(contour, True)
        approximate_polygon = cv2.approxPolyDP(contour, epsilon_arc, True)
        return len(approximate_polygon) == self.edges_count

    def filter(self, contours: [ndarray]) -> [ndarray]:
        return [contour for contour in contours if self.__check_contour_shape(contour)]
