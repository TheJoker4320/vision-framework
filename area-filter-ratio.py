import cv2
from IFilter import IFilter
import utils

"""Gets the countours and filters them by area ratio range """
class AreaRatioFilter(IFilter):

    def __init__(self, min_area_ratio, max_area_ratio):
        self.min_area_ratio = min_area_ratio
        self.max_area_ratio = max_area_ratio
        
    def filter(self, conts):
        lst = []
        for cont in conts:
            rect = cv2.minAreaRect(cont)
            p0, p1, p2, p3 = cv2.boxPoints(rect)
            h = utils.distance(p0, p1)
            w = utils.distance(p1, p2)
            rect_area = w * h
            area = cv2.contourArea(cnt)

            if self.max_area_ratio >= float(rect_area) / area >= self.min_area_ratio:
                lst.append(cont)
        return lst
