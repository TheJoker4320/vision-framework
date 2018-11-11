import math
import cv2


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def find_center(contour):
    moment = cv2.moments(contour)
    center_x = int(moment['m10'] / moment['m00'])
    center_y = int(moment['m01'] / moment['m00'])
    return center_x, center_y


def calculate_focal_length(image_width, horizontal_field_of_view):
    return image_width / (
        2 * math.tan(math.radians(horizontal_field_of_view / 2)))
