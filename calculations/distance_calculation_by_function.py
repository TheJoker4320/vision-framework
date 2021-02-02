from calculations.calculation import Calculation
from numpy import ndarray
import cv2
import calculation_utils


class DistanceCalculationByFunction(Calculation):
    """
    Calculates the distance between the camera and the object.
    Uses self made distance calculation function
         where f(x) is the real distance of the camera from the object
         and x is the image's height in pixels (imaginary_height).
    """

    distance_function: str

    def __init__(self, distance_function: str):
        """
        :param distance_function: self made distance calculation function, where f(x) is the real distance of the
                                  camera from the object and x is the image's height in pixels (imaginary_height).
        :type distance_function: str
        """
        self.distance_function = distance_function

    def calc(self, contours: [ndarray]) -> dict:
        data_dictionary = {}

        # Merge all contours and refers to them as one
        merged_cont = calculation_utils.merge_contours(contours)

        # Block the merged contour with a rectangle
        rectangle = cv2.minAreaRect(merged_cont)
        # Get it's points
        _, p1, p2, _ = cv2.boxPoints(rectangle)
        # Calculate the height of the rectangle (in pixels)
        imaginary_height = calculation_utils.distance(p1, p2)

        # Set the imaginary_height in the given function (as an x)
        distance = eval(self.distance_function, {}, {"imaginary_height": imaginary_height})

        data_dictionary['distance'] = distance

        return data_dictionary
