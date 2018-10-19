from ICalculation import ICalculation
import math
import utils


class AngleCalculation(ICalculation):
    """
    Calculate the x and y angels between the camera and the object in the image
    """

    def __init__(self, image_width, horizontal_field_of_view, image_x_center, image_y_center):
        self.image_width = image_width
        self.horizontal_field_of_view = horizontal_field_of_view
        self.image_x_center = image_x_center
        self.image_y_center = image_y_center

    def calc(self, contour):
        dictionary = {}
        x_center, y_center = utils.find_center(contour)
        focal_length = utils.calculate_focal_length(self.image_width, self.horizontal_field_of_view)

        x_angle = math.atan((x_center - self.image_x_center) / focal_length)
        x_angle = math.degrees(x_angle)
        y_angle = math.atan((y_center - self.image_y_center) / focal_length)
        y_angle = math.degrees(y_angle)

        dictionary["x_angle"] = x_angle
        dictionary["y_angle"] = y_angle
        return dictionary
