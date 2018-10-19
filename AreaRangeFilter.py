from IFilter import IFilter
import cv2


class AreaRangeFilter(IFilter):

    def __init__(self, min_area, max_area):
        self.min_area = min_area
        self.max_area = max_area

    def filter(self, contours):
        new_cnt = []
        for cnt in contours:
            area = cv2.countourArea(cnt)
            if self.min_area <= area <= self.max_area:
                new_cnt.append(cnt)
        return new_cnt
