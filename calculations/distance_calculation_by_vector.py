from calculations.calculation import Calculation
import cv2
import numpy as np
import calculation_utils


class DistanceCalculationByVector(Calculation):
    """
    Calculates the distance between the camera and the object
    Uses the image's width, camera's field of view and the object's height in reality
    """

    def __init__(self, field_of_view, image_width, image_height, object_surface_area, yaw_angle=0, pitch_angle=0,
                 roll_angle=0, x_offset=0, y_offset=0, z_offset=0):
        """
        :param field_of_view:
        :param image_width:
        offsets are the distance in each axis away from the center of the robot
        yaw_angle is the clockwise yaw angle (in radians) in which the camera is rotated, the yaw angle is the angle around the y axis,
        pitch_angle is the clockwise pitch angle (in radians) in which the camera is rotated, the pitch angle is the angle around the x axis,
        roll_angle is the clockwise roll angle (in radians) in which the camera is rotated, the roll angle is the angle around the z axis
        """
        self.field_of_view = field_of_view
        self.image_width = image_width
        self.image_height = image_height
        self.object_surface_area = object_surface_area
        self.focal_length = calculation_utils.calculate_focal_length(image_width, field_of_view)
        self.yaw_angle = yaw_angle
        self.pitch_angle = pitch_angle
        self.roll_angle = roll_angle
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.z_offset = z_offset

    def calc(self, contours):
        data_dictionary = {}

        merged_cont = calculation_utils.merge_contours(contours)
        cont_area = cv2.contourArea(merged_cont)
        x_object_center, y_object_center = calculation_utils.find_center(contours)

        x_frame_center = self.image_width / 2
        y_frame_center = self.image_height / 2

        x_vector = x_frame_center - x_object_center
        y_vector = y_frame_center - y_object_center

        alpha = x_vector * self.focal_length / x_frame_center
        beta = y_vector * self.focal_length / y_frame_center

        # the norm of the vector between the camera and the object (in meters)
        distance_vector = self.focal_length * self.object_surface_area / cont_area

        rel = np.array([[np.sin(alpha), np.sin(beta),
                         np.sqrt(1 - np.sin(alpha) ** 2 - np.sin(beta) ** 2)]]) * distance_vector

        offset = np.array([self.x_offset, self.y_offset, self.z_offset])
        rotation_matrix = self.create_rotation_matrix()

        """
        normal_distance_vector = self.focal_length*math.sqrt(object_surface_area/cont_area)

        distance_from_image_center_x = int(self.image_width)/2 - x_center
        distance_from_image_center_y = int(self.image_height)/2 - y_center
        distance_x = normal_distance_vector * math.sin(self.field_of_view)*(2)
        distance_y = normal_distance_vector * math.sin(self.field_of_view)*(2/self.image_width)

        # x^2 + y^2 + z^2 = normal_distance_vector^2
        distance = math.sqrt(math.pow(normal_distance_vector,2) - math.pow(distance_x,2) - math.pow(distance_y,2))
        """
        # a 3d vector of the relative [x y z] location between the object and the camera (in meters)
        distance = rotation_matrix.dot(rel.T).flatten() + offset
        data_dictionary['distance'] = distance

        return data_dictionary

    def create_rotation_matrix(self):
        sin, cos = np.sin(self.yaw_angle), np.cos(self.yaw_angle)
        rotation_matrix = np.array([[cos, 0, sin],
                                    [0, 1, 0],
                                    [-sin, 0, cos]])
        sin, cos = np.sin(self.pitch_angle), np.cos(self.pitch_angle)
        rotation_matrix = rotation_matrix.dot(np.array([[1, 0, 0],
                                                        [0, cos, -sin],
                                                        [0, sin, cos]]))
        sin, cos = np.sin(self.roll_angle), np.cos(self.roll_angle)
        rotation_matrix = rotation_matrix.dot(np.array([[cos, -sin, 0],
                                                        [sin, cos, 0],
                                                        [0, 0, 1]]))
        return rotation_matrix
