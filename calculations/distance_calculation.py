from calculations.calculation import Calculation
import cv2
import calculation_utils


class DistanceCalculation(Calculation):
    """
    Calculates the distance between the camera and the object
    Uses self made distance calculation function
    """

    def __init__(self, calc_constant):
        self.calc_constant = calc_constant

    def calc(self, contours):
        data_dict = {}
        merged_cont = calculation_utils.merge_contours(contours)
        rectangle = cv2.minAreaRect(merged_cont)
        _, p1, p2, _ = cv2.boxPoints(rectangle)
        imaginary_height = calculation_utils.distance(p1, p2)
        distance = self.calc_constant / imaginary_height
        data_dict['distance'] = distance
        return data_dict
