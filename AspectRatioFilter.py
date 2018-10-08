from IFilter import IFilter
import cv2
import math


class AspectRatioFilter(IFilter):

    def __init__(self, min_ratio, max_ratio):
        self.min_ratio = min_ratio
        self.max_ratio = max_ratio

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def filter(self, conts):
        lst = []
        for cont in conts:
            rect = cv2.minAreaRect(cont)
            p0, p1, p2, p3 = cv2.boxPoints(rect)
            h = self.distance(p0, p1)
            w = self.distance(p1, p2)
            ratio = float(max(h, w))/min(h, w)

            if self.min_ratio <= ratio <= self.max_ratio:
                lst.append(cont)
        return lst
