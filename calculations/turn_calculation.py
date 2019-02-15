from calculation import Calculation
from distance_calculation import DistanceCalculation
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
            shorter_distance = min(dis_from_contour1, dis_from_contour2)

            merge_contours = calculation_utils.merge_contours([contour1, contour2])
            dis_from_center = distance_calculation.calc([merge_contours])['distance']

            angle = math.acos((math.pow(dis_from_center, 2) + math.pow(self.tape_width, 2) - math.pow(shorter_distance, 2)) / (2 * dis_from_center * self.tape_width))
            before_turn = dis_from_center * math.cos(angle)
            after_turn = dis_from_center * math.sin(angle)
            dictionary = {"before turn": before_turn, "after turn": after_turn, "angle": angle * 180 / math.pi}
            return dictionary
        else:
            return {}
