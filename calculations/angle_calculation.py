from calculations.calculation import Calculation
from numpy import ndarray
import math
import calculation_utils


class AngleCalculation(Calculation):
    """
    Calculate the x and y angels between the camera and the object in the image.
    Uses the image's width, horizontal field of view and x/y values of the center.
    """

    image_width: float
    horizontal_field_of_view: float
    image_x_center: float
    image_y_center: float
    focal_length: float

    def __init__(self, image_width: float, horizontal_field_of_view: float, image_x_center: float,
                 image_y_center: float):
        """
        :param image_width: The width of the image (in pixels)
        :type image_width: float

        :param horizontal_field_of_view: The field of view on the horizontal axis (in degrees)
        :type horizontal_field_of_view: float

        :param image_x_center: The image x center
        :type image_x_center: float

        :param image_y_center: The image y center
        :type image_y_center: float
        """
        self.image_width = image_width
        self.horizontal_field_of_view = horizontal_field_of_view
        self.image_x_center = image_x_center
        self.image_y_center = image_y_center
        self.focal_length = calculation_utils.calculate_focal_length(self.image_width, self.horizontal_field_of_view)

    def calc(self, contours: [ndarray]) -> dict:
        angles_degrees = {}

        # Merge all contours and refers to them as one
        merged_cont = calculation_utils.merge_contours(contours)
        # Find the merge-contour-center's coordinates
        x_center, y_center = calculation_utils.find_center(merged_cont)

        # Calculate the angels across the x and y axises
        x_angle_degrees = self.angle_calc(x_center, self.image_x_center)
        y_angle_degrees = self.angle_calc(y_center, self.image_y_center)

        angles_degrees["x_angle"] = x_angle_degrees
        angles_degrees["y_angle"] = y_angle_degrees
        return angles_degrees

    def angle_calc(self, center: float, image_center: float) -> float:
        """
        Calculates the angle using a given counter's center and an image center

        :param center: The x or y center
        :type center: float

        :param image_center: The image x or y center
        :type image_center: float

        :return: The angle in degrees
        :rtype: float
        """
        angle_radians = math.atan((center - image_center) / self.focal_length)
        return math.degrees(angle_radians)
