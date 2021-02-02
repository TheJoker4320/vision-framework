from calculations.calculation import Calculation
from numpy import ndarray
import cv2
import math
import calculation_utils


class DistanceCalculationByArea(Calculation):
    """
    Calculates the distance between the camera and the object.
    Uses the image's width, camera's field of view and the object's area in reality.
    """

    focal_length: float
    real_area: float

    def __init__(self, field_of_view: float, image_width: int, real_area: float):
        """
        :param field_of_view: The fov of the camera (in degrees)
        :type field_of_view: float

        :param image_width: The width of the image (in pixels)
        :type image_width: float

        :param real_area: The real area of the object
        :type real_area: float
        """
        self.focal_length = calculation_utils.calculate_focal_length(image_width, field_of_view)
        self.real_area = real_area

    def calc(self, contours: [ndarray]) -> dict:
        data_dictionary = {}

        # Merge all contours and refers to them as one
        merged_cont = calculation_utils.merge_contours(contours)
        # Calculate the merged-contour's area
        cont_area = cv2.contourArea(merged_cont)
        # Calculate the square ratio between the merged-contour's area and the object's real area
        ratio = math.sqrt(cont_area / self.real_area)
        # Calculate the distance
        distance = ratio * self.focal_length
        data_dictionary['distance'] = distance

        return data_dictionary
