from filters.filter import Filter
import sys
import cv2
import calculation_utils
import numpy_utils


class DiagonalReflectiveTapePair(Filter):
    """
    Goes over all the contours returns the two that turn to each other
    Matches to the 2019 requirements
    """

    def __find_two_highest_points(self, contour):
        """
        WIP
        :param contour:
        :return:
        """
        rectangle = cv2.minAreaRect(contour)
        points = cv2.boxPoints(rectangle)
        higher_point = min(points, key=lambda point: point[1])
        # points.remove(higher_point)
        points = numpy_utils.remove(points, higher_point)
        lower_point = min(points, key=lambda point: point[1])
        return higher_point, lower_point

    def filter(self, contours):
        shortest_higher_distance = sys.maxint
        return_contours = []

        for contour1 in contours:
            # find the two highest points
            higher_point_1, lower_point_1 = self.__find_two_highest_points(contour1)
            for contour2 in contours:
                # find the two highest points
                higher_point_2, lower_point_2 = self.__find_two_highest_points(contour2)
                # calculate the distances
                higher_distance = calculation_utils.distance(higher_point_1, higher_point_2)
                lower_distance = calculation_utils.distance(lower_point_1, lower_point_2)

                if shortest_higher_distance >= higher_distance > lower_distance:
                    return_contours.append(contour1)
                    return_contours.append(contour2)
                    shortest_higher_distance = higher_distance

        return return_contours
