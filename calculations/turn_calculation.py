from calculation import Calculation
from distance_calculation import DistanceCalculation
import math
import calculation_utils


class TurnCalculation(Calculation):
    """

    """

    def __init__(self, field_of_view, image_width, real_height, tape_width):
        self.real_height = real_height
        self.field_of_view = field_of_view
        self.image_width = image_width
        self.tape_width = tape_width

    def calc(self, contours):
        if len(contours) == 2:
            contour1 = contours[0]
            contour2 = contours[1]
            distanceCalculation = DistanceCalculation(self.field_of_view, self.image_width, self.real_height)
            disFromContour1 = distanceCalculation.calc(contour1)['distance']
            disFromContour2 = distanceCalculation.calc(contour2)['distance']
            shorter_distance = min(disFromContour1, disFromContour2)

            merge_contours = calculation_utils.merge_contours(contour1, contour2)
            disFromCenter = distanceCalculation.calc(merge_contours)['distance']

            angle = math.acos((math.pow(disFromCenter, 2) + math.pow(self.tape_width, 2) - math.pow(shorter_distance, 2)) / (2 * disFromCenter * self.tape_width))
            before_turn = disFromCenter * math.cos(angle)
            after_turn = disFromCenter * math.sin(angle)
            dictionary = {"before turn": before_turn, "after turn": after_turn, "angle": angle * 180 / math.pi}
            return dictionary
        else:
            return {}
