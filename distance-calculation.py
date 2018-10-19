from ICalculation import ICalculation
import cv2
import math


class DistanceCalculation(ICalculation):
    """
    Calculates the distance between the camera and the object
    """

    def __init__(self, field_of_view,image_width, real_hight):
        self.focal_length = utils.calculate_focal_length(image_width, field_of_view)
        self.real_hight = real_hight

    def calc(self, contour):
        dic = {}
        p0, p1, p2, p3 = cv2.boxPoints(rect)
        h = utils.distance(p0, p1)
        w = utils.distance(p1, p2)
        dist = float(self.real_hight) / max(h, w) * self.focal_length
        dic['distance'] = dist
        return dist
