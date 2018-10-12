import cv2
from IFilter import IFilter


class AreaRatioFilter(IFilter):

    def __init__(self, min_area_ratio, max_area_ratio):
        self.min_area_ratio = min_area_ratio
        self.max_area_ratio = max_area_ratio
        
    def filter(self, conts):
        lst = []
        for cont in conts:
            rect = cv2.minAreaRect(cont)
            p0, p1, p2, p3 = cv2.boxPoints(rect)
            h = self.distance(p0, p1)
            w = self.distance(p1, p2)
            rect_area = w * h
            area = cv2.contourArea(cnt)

            if  max_area_ratio >= float(rect_area) / area >= min_area_ratio:
                lst.append(cont)
        return lst
