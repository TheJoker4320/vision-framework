import cv2
from IFilter import IFilter
import utils

""" Gets the contours and filters them by area ratio range """


class AreaRatioFilter(IFilter):

    def __init__(self, min_area_ratio, max_area_ratio):
        self.min_area_ratio = min_area_ratio
        self.max_area_ratio = max_area_ratio

    def filter(self, cnts):
        lst = []
        for cnt in cnts:
            rect = cv2.minAreaRect(cnt)
            point1, point2, point3, point4 = cv2.boxPoints(rect)
            reg_height = utils.distance(point1, point2)
            reg_width = utils.distance(point3, point4)
            rect_area = reg_width * reg_height
            cnt_area = cv2.contourArea(cnt)  # The contour area

            if self.max_area_ratio >= float(rect_area) / cnt_area >= \
                    self.min_area_ratio:
                lst.append(cnt)
        return lst
