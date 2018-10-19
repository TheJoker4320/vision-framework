from IFilter import IFilter
import cv2

"""Filters the shape by the number of edges and epsilon"""


class ShapeFilter(IFilter):
    def __init__(self, edges, epsilon):
        self.edges = edges
        self.epsilon = epsilon

    def filter(self, contours):
        lst = []
        for cont in contours:
            epsilon_arc = self.epsilon * cv2.arcLength(cont, True)
            approx = cv2.approxPolyDP(cont, epsilon_arc, True)
            if len(approx) == self.edges:
                lst.append(cont)
        return lst
