from IFilter import IFilter
import cv2
import utils


class AspectRatioFilter(IFilter):

    def __init__(self, min_ratio, max_ratio):
        self.min_ratio = min_ratio
        self.max_ratio = max_ratio

    def filter(self, conts):
        lst = []
        for cont in conts:
            rect = cv2.minAreaRect(cont)
            p0, p1, p2, p3 = cv2.boxPoints(rect)
            h = utils.distance(p0, p1)
            w = utils.distance(p1, p2)
            ratio = float(max(h, w))/min(h, w)

            if self.min_ratio <= ratio <= self.max_ratio:
                lst.append(cont)
        return lst
