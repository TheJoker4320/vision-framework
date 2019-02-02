from calculation import Calculation
import calculation_utils
import distance_calculation
import math


class TurnCalculation(Calculation):
    """

    """

    def __init__(self, field_of_view, image_width, real_height, tape_width):
        self.real_height = real_height
        self.field_of_view = field_of_view
        self.image_width = image_width
        self.tape_width = tape_width

    def calc(self, contours):
        cntr1 = contours[0]
        cntr2 = contours[1]

        disFromP1toP2 = distance_calculation(self.field_of_view, self.image_width, self.real_height).calc(cntr1)['distance']
        disFromP1toP3 = distance_calculation(self.field_of_view, self.image_width, self.real_height).calc(cntr2)['distance']
        height1 = max(disFromP1toP2, disFromP1toP3)

        disFromP1toP2 = distance_calculation.distance(contour2[0], contour2[1])
        disFromP1toP3 = distance_calculation.distance(contour2[0], contour2[2])
        height2 = max(disFromP1toP2, disFromP1toP3)

        height = min(height1, height2)
        merge_contours = calculation_utils.merge_contours(contour1, contour2)
        disFromCenter = distance_calculation(self.field_of_view, self.image_width, self.real_height).calc(merge_contours)['distance']

        angle = math.acos((math.pow(disFromCenter, 2) + math.pow(self.tape_width, 2) - math.pow(height, 2))/(2 * disFromCenter * self.tape_width))
        before_turn = disFromCenter*math.cos(angle)
        after_turn = disFromCenter*math.sin(angle)
        dictionary = {"before turn": before_turn, "after turn": after_turn, "angle": angle*180/math.pi}
        return dictionary
