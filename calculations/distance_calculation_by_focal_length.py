from calculations.calculation import Calculation
from numpy import ndarray
import cv2
import calculation_utils


class DistanceCalculationByFocalLength(Calculation):
    """
    Calculates the distance between the camera and the object.
    Uses the image's width, camera's field of view and the object's height in reality.
    """

    focal_length: float
    real_height: float

    def __init__(self, field_of_view: float, image_width: float, real_height: float):
        """
        :param field_of_view: The fov of the camera (in degrees)
        :type field_of_view: float

        :param image_width: The width of the image (in pixels)
        :type image_width: float

        :param real_height: The real height of the object (in meters)
        :type real_height: float
        """
        self.focal_length = calculation_utils.calculate_focal_length(image_width, field_of_view)
        self.real_height = real_height

    def calc(self, contours: [ndarray]) -> dict:
        data_dictionary = {}

        # Merge all contours and refers to them as one
        merged_cont = calculation_utils.merge_contours(contours)

        # Block the merged contour with a rectangle
        rectangle = cv2.minAreaRect(merged_cont)
        # Get it's points
        p0, p1, p2, p3 = cv2.boxPoints(rectangle)
        # Calculate the sides of the rectangle
        side1_length = calculation_utils.distance(p0, p1)
        side2_length = calculation_utils.distance(p1, p2)

        # Get the height of the rectangle (suppose to be the bigger side)
        rectangle_height = max(side1_length, side2_length)
        # Calculate the distance using it
        distance = float(self.real_height) / rectangle_height * self.focal_length
        data_dictionary['distance'] = distance

        return data_dictionary
