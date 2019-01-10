from filter import Filter
import cv2
import calculation_utils


class DiagonalReflectiveTapePair(filter):
    """
    Goes over all the contours the two that turn to each other
    matches to the 2019 requirements
    the
    """

    def __init__(self):
        pass

    def __find_two_highest_points(self, contour):
        rectangle = cv2.minAreaRect(contour)
        points = cv2.boxPoints(rectangle)
        higher_point = max(points, key=lambda point: point[1])
        points.remove(higher_point)
        lower_point = max(points, key=lambda point: point[1])
        return higher_point, lower_point

    def filter(self, contours):

        for contour1 in contours:
            # find the two highest points
            higher_point_1, lower_point_1 = self.__find_two_highest_points(contour1)
            for contour2 in contours:
                # find the two highest points
                higher_point_2, lower_point_2 = self.__find_two_highest_points(contour2)
                # calculate the distances
                higher_distance = calculation_utils.distance(higher_point_1, higher_point_2)
                lower_distance = calculation_utils.distance((lower_point_1, lower_point_2))

                if higher_distance > lower_distance:
                    return [contour1, contour2]
        return []
