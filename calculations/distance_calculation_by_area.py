from calculation import Calculation
import cv2
import math
import calculation_utils


class DistanceCalculation(Calculation):
    """
    Calculates the distance between the camera and the object
    Uses the image's width, camera's field of view,
    and the object's height in reality.
    """

    def __init__(self, field_of_view, image_width, real_area):
        self.focal_length = calculation_utils.calculate_focal_length(image_width, field_of_view)
        self.real_area = real_area

    def calc(self, contours):
        data_dictionary = {}

        merged_cont = calculation_utils.merge_contours(contours)
        cont_area = cv2.contourArea(merged_cont)
        ratio = math.sqrt(cont_area / self.real_area)
        distance = ratio * self.focal_length
        data_dictionary['distance'] = distance

        return data_dictionary
