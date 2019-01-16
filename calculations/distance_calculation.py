from calculation import Calculation
import cv2
import calculation_utils


class DistanceCalculation(Calculation):
    """
    Calculates the distance between the camera and the object
    Uses the image's width, camera's field of view,
    and the object's height in reality.
    """

    def __init__(self, field_of_view, image_width, real_height):
        self.focal_length = calculation_utils.calculate_focal_length(image_width, field_of_view)
        self.real_height = real_height

    def calc(self, contour):
        data_dictionary = {}

        rectangle = cv2.minAreaRect(contour)
        p0, p1, p2, p3 = cv2.boxPoints(rectangle)
        side1_length = calculation_utils.distance(p0, p1)
        side2_length = calculation_utils.distance(p1, p2)

        rectangle_height = max(side1_length, side2_length)
        distance = float(self.real_height) / rectangle_height * self.focal_length
        data_dictionary['distance'] = distance

        return data_dictionary
