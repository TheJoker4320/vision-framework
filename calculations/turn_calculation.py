from calculations.calculation import Calculation
from calculations.distance_calculation import DistanceCalculation
import math
import calculation_utils


class TurnCalculation(Calculation):
    """
    WIP
    """

    def __init__(self, field_of_view, image_width, real_height, tape_width):
        """
        :param field_of_view:
        :param image_width:
        :param real_height:
        :param tape_width:
        """
        self.real_height = real_height
        self.field_of_view = field_of_view
        self.image_width = image_width
        self.tape_width = tape_width

    def calc(self, contours):
        if len(contours) == 2:
            contour1 = contours[0]
            contour2 = contours[1]
            distance_calculation = DistanceCalculation(self.field_of_view, self.image_width, self.real_height)
            dis_from_contour1 = distance_calculation.calc([contour1])['distance']
            dis_from_contour2 = distance_calculation.calc([contour2])['distance']
            short_dist = min(dis_from_contour1, dis_from_contour2)
            long_dist = max(dis_from_contour1, dis_from_contour2)

            merge_contours = calculation_utils.merge_contours([contour1, contour2])
            dis_from_center = distance_calculation.calc([merge_contours])['distance']
            angle = math.acos(
                (long_dist ** 2 + self.tape_width ** 2 - short_dist ** 2) / (2 * long_dist * self.tape_width))
            angle = angle + 0.5 * math.pi
            half_tape_distance = self.tape_width / 2
            second_run = math.tan(angle) * half_tape_distance
            first_run = second_run * math.cos(angle) + math.sqrt(
                second_run ** 2 * math.cos(angle) - second_run ** 2 + dis_from_center ** 2)
            return {"angle": math.degrees(angle), "first distance": first_run, "second distance": second_run}
        else:
            return {}
