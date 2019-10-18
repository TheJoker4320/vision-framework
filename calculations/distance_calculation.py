from calculations.calculation import Calculation
import cv2
import calculation_utils


class DistanceCalculation(Calculation):
    """
    Calculates the distance between the camera and the object
    Uses self made distance calculation function
         where y is the real distance of the camera from the object
         and x is the image's height in pixels (imaginary_height)
    """

    def __init__(self, distance_function):
        """
        :param distance_function:
        """
        self.distance_function = distance_function

    def calc(self, contours):
        data_dictionary = {}

        merged_cont = calculation_utils.merge_contours(contours)
        rectangle = cv2.minAreaRect(merged_cont)
        _, p1, p2, _ = cv2.boxPoints(rectangle)
        imaginary_height = calculation_utils.distance(p1, p2)
        distance = eval(self.distance_function)
        data_dictionary['distance'] = distance

        return data_dictionary
