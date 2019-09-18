from calculations.calculation import Calculation
import cv2
import calculation_utils


class DistanceCalculation(Calculation):
    """
    Calculates the distance between the camera and the object
    Uses self made distance calculation function
    """

    def calc(self, contours):
        data_dict = {}
        merged_cont = calculation_utils.merge_contours(contours)
        rectangle = cv2.minAreaRect(merged_cont)
        _, p1, p2, _ = cv2.boxPoints(rectangle)
        height = calculation_utils.distance(p1, p2)
        distance = self.distance_calc(height)
        data_dict['distance'] = distance
        return data_dict

    def distance_calc(self, height):
        """
        WIP
        :param height: The height of the given object
        :return: The distance between the camera and the object
        """
        distance = height
        return distance
