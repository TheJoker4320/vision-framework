import cv2
from IFilter import IFilter


class BiggestAreaFilter(IFilter):
    def __init__(self):
        pass

    def filter(self, contours):
        return [max(contours, key=cv2.contourArea)]
