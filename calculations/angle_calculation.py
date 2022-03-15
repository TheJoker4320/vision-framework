from calculations.calculation import Calculation
import math
import calculation_utils


class AngleCalculation(Calculation):
    """
    Calculate the x and y angels between the camera and the object in the image
    Uses the image's width, horizontal field of view and x/y values of the center
    """

    def __init__(self, image_width, horizontal_field_of_view, image_x_center, image_y_center):
        self.image_width = image_width
        self.horizontal_field_of_view = horizontal_field_of_view
        self.image_x_center = image_x_center
        self.image_y_center = image_y_center
        self.focal_length = calculation_utils.calculate_focal_length(self.image_width, self.horizontal_field_of_view)

    def calc(self, contours):
        angles_degrees = {}
        merged_cont = calculation_utils.merge_contours(contours)
        x_center, y_center = calculation_utils.find_center(merged_cont)

        x_angle_degrees = self.angle_calc(x_center, self.image_x_center)
        y_angle_degrees = self.angle_calc(y_center, self.image_y_center)

        angles_degrees["x_angle"] = x_angle_degrees
        angles_degrees["y_angle"] = y_angle_degrees
        return angles_degrees

    def angle_calc(self, center, image_center):
        """
        :param center: The x or y center
        :param image_center: The image x or y center
        :return: The angle in degrees
        """
        angle_radians = math.atan((center - image_center) / self.focal_length)
        return math.degrees(angle_radians)
