from calculations.calculation import Calculation
from calculations.distance_calculation_by_focal_length import DistanceCalculationByFocalLength
from numpy import ndarray
import math
import calculation_utils


class TurnCalculation(Calculation):
    """
    Calculate the distance of the 2 edges of a triangle (those are the two relevant distance) and the third edge is the
    direct distance, and calculate the angle needed to turn to get to the first edge's position.
    Uses the image's width and height, camera's field of views, the object's height in reality and the diagonal
    reflective tape's width.
    Matches to the 2019 requirements
    """

    field_of_view: float
    image_width: float
    real_height: float
    tape_width: float

    def __init__(self, field_of_view: float, image_width: float, real_height: float, tape_width: float):
        """
        :param field_of_view: The fov of the camera (in degrees)
        :type field_of_view: float

        :param image_width: The width of the image (in pixels)
        :type image_width: float

        :param real_height: The real height of the object (in meters)
        :type real_height: float

        :param tape_width: The tape tape width (in meters)
        :type tape_width: float
        """
        self.field_of_view = field_of_view
        self.image_width = image_width
        self.real_height = real_height
        self.tape_width = tape_width

    def calc(self, contours: [ndarray]) -> dict:

        # Check if there are exactly 2 contours
        if len(contours) == 2:
            # Set the contours
            contour1 = contours[0]
            contour2 = contours[1]

            # Calculate the distance of the each contour
            distance_calculation = DistanceCalculationByFocalLength(self.field_of_view, self.image_width, self.real_height)
            dis_from_contour1 = distance_calculation.calc([contour1])['distance']
            dis_from_contour2 = distance_calculation.calc([contour2])['distance']

            # Set the short and long distances
            short_dist = min(dis_from_contour1, dis_from_contour2)
            long_dist = max(dis_from_contour1, dis_from_contour2)

            # Merge the contours and refers to them as one
            merge_contours = calculation_utils.merge_contours([contour1, contour2])
            # Calculate the distance from the contour
            dis_from_center = distance_calculation.calc([merge_contours])['distance']
            # Calculate the angle
            angle = math.acos(
                (long_dist ** 2 + self.tape_width ** 2 - short_dist ** 2) / (2 * long_dist * self.tape_width))
            angle = angle + 0.5 * math.pi

            # Calculate the two distances that the robot need to move
            half_tape_distance = self.tape_width / 2
            second_run = math.tan(angle) * half_tape_distance
            first_run = second_run * math.cos(angle) + math.sqrt(
                second_run ** 2 * math.cos(angle) - second_run ** 2 + dis_from_center ** 2)
            return {"angle": math.degrees(angle), "first distance": first_run, "second distance": second_run}
        else:
            return {}
