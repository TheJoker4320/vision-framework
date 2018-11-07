from IFilter import IFilter
import cv2


class ShapeFilter(IFilter):
    """
    responsible for  filtering contours by their approximate shape
    check the approximate shape according to epsilon value
    as epsilon is bigger the filtering is more flexible
    """

    def __init__(self, edges_count, epsilon):
        self.edges_count = edges_count
        self.epsilon = epsilon

    def __is_similar_shape(self, contour):
        """

        :param contour: the contour to
        :type contour: the contour to check
        :return: is the contour is approximately similar to the type of shape
        (by number of edges)
        :rtype: boolean
        """
        epsilon_arc = self.epsilon * cv2.arcLength(contour, True)
        approximate_polygon = cv2.approxPolyDP(contour, epsilon_arc, True)
        return len(approximate_polygon) == self.edges_count

    def filter(self, contours):
        return [contour for contour in contours if
                self.__is_similar_shape(contour)]
