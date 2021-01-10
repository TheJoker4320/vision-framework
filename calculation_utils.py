import math
import cv2
import numpy


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def find_center(contour):
    moment = cv2.moments(contour)
    center_x = int(moment['m10'] / moment['m00'])
    center_y = int(moment['m01'] / moment['m00'])
    return center_x, center_y


def calculate_focal_length(image_width, horizontal_field_of_view):
    return image_width / (2 * math.tan(math.radians(horizontal_field_of_view / 2)))


def merge_contours(contours):
    if len(contours) == 1:
        return contours[0]

    left_extreme_points = [__get_left_extreme_point(contour) for contour in contours]
    right_extreme_points = [__get_right_extreme_point(contour) for contour in contours]
    top_extreme_points = [__get_top_extreme_point(contour) for contour in contours]
    bottom_extreme_points = [__get_bottom_extreme_point(contour) for contour in contours]

    left_extreme_point = min(left_extreme_points, key=lambda point: point[0])
    right_extreme_point = max(right_extreme_points, key=lambda point: point[0])
    top_extreme_point = min(top_extreme_points, key=lambda point: point[1])
    bottom_extreme_point = max(bottom_extreme_points, key=lambda point: point[1])

    p0 = numpy.array([left_extreme_point[0], top_extreme_point[1]])
    p1 = numpy.array([right_extreme_point[0], top_extreme_point[1]])
    p2 = numpy.array([right_extreme_point[0], bottom_extreme_point[1]])
    p3 = numpy.array([left_extreme_point[0], bottom_extreme_point[1]])

    merged_contour = numpy.array([p0, p1, p2, p3])
    return merged_contour


def create_rotation_matrix(yaw_angle, pitch_angle, roll_angle):
    sin, cos = numpy.sin(yaw_angle), numpy.cos(yaw_angle)
    rotation_matrix = numpy.array([[cos, 0, sin],
                                   [0, 1, 0],
                                   [-sin, 0, cos]])
    sin, cos = numpy.sin(pitch_angle), numpy.cos(pitch_angle)
    rotation_matrix = rotation_matrix.dot(numpy.array([[1, 0, 0],
                                                       [0, cos, -sin],
                                                       [0, sin, cos]]))
    sin, cos = numpy.sin(roll_angle), numpy.cos(roll_angle)
    rotation_matrix = rotation_matrix.dot(numpy.array([[cos, -sin, 0],
                                                       [sin, cos, 0],
                                                       [0, 0, 1]]))
    return rotation_matrix


def __get_left_extreme_point(contour):
    return tuple(contour[contour[:, :, 0].argmin()][0])


def __get_right_extreme_point(contour):
    return tuple(contour[contour[:, :, 0].argmax()][0])


def __get_top_extreme_point(contour):
    return tuple(contour[contour[:, :, 1].argmin()][0])


def __get_bottom_extreme_point(contour):
    return tuple(contour[contour[:, :, 1].argmax()][0])
