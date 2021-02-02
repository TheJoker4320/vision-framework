from calculations.calculation import Calculation
import cv2
import math
import logging
import numpy as np
import calculation_utils


class DistanceCalculationByVector(Calculation):
    """
    Calculates the distance between the camera and the object across the x, y and z axises.
    Uses the image's width and height, camera's field of views, the object's surface area in reality and the camera's
    location relative to the robot.
    """

    horizontal_field_of_view: float
    vertical_field_of_view: float
    image_width: float
    image_height: float
    sqrt_object_area: float
    focal_length: float
    offset: np.ndarray
    rotation_matrix: np.ndarray

    def __init__(self, horizontal_field_of_view: float, vertical_field_of_view: float, image_width: float,
                 image_height: float, object_surface_area: float, yaw_angle: float = 0, pitch_angle: float = 0,
                 roll_angle: float = 0, x_offset: float = 0, y_offset: float = 0, z_offset: float = 0):
        """
        :param horizontal_field_of_view: the field of view on the horizontal axis (in degrees)
        :type horizontal_field_of_view: float

        :param vertical_field_of_view: the field of view on the vertical axis (in degrees)
        :type vertical_field_of_view: float

        :param image_width: the width of the image (in pixels)
        :type image_width: int

        :param image_height: the height of the image (in pixels)
        :type image_height: int

        :param yaw_angle: the clockwise yaw angle (in degrees) in which the camera is rotated, the yaw angle is the
                          angle around the y axis (default is 0.0)
        :type yaw_angle: float
        :param pitch_angle: the clockwise pitch angle (in degrees) in which the camera is rotated, the yaw angle is the
                            angle around the x axis (default is 0.0)
        :type pitch_angle: float
        :param roll_angle: the clockwise roll angle (in degrees) in which the camera is rotated, the roll angle is the
                           angle around the z axis (default is 0.0)
        :type roll_angle: float


        :param x_offset: the distance (in meters) in the x axis away from the center of the robot (default is 0.0)
        :type x_offset: float

        :param y_offset: the distance (in meters) in the y axis away from the center of the robot (default is 0.0)
        :type y_offset: float

        :param z_offset: the distance (in meters) in the z axis away from the center of the robot (default is 0.0)
        :type z_offset: float
        """
        self.horizontal_field_of_view = horizontal_field_of_view
        self.vertical_field_of_view = vertical_field_of_view
        self.image_width = image_width
        self.image_height = image_height
        self.sqrt_object_area = math.sqrt(object_surface_area)
        self.focal_length = calculation_utils.calculate_focal_length(image_width, horizontal_field_of_view)

        self.offset = np.array([x_offset, y_offset, z_offset])
        self.rotation_matrix = calculation_utils.create_rotation_matrix(np.radians(yaw_angle), np.radians(pitch_angle),
                                                                        np.radians(roll_angle))

    def calc(self, contours: [np.ndarray]) -> dict:
        data_dictionary = {}

        # Merge all contours and refers to them as one
        merged_cont = calculation_utils.merge_contours(contours)

        # Find the merged-contour's square root (in pixels)
        sqrt_cont_area = math.sqrt(cv2.contourArea(merged_cont))

        # Find the merge-contour-center's coordinates
        x_cont_center, y_cont_center = calculation_utils.find_center(merged_cont)
        # Find the frame-center's coordinates
        x_frame_center, y_frame_center = self.image_width / 2, self.image_height / 2

        # Find x and y vectors from frame-center's coordinates to the merge-contour-center's coordinates
        x_vector, y_vector = x_cont_center - x_frame_center, y_cont_center - y_frame_center

        # Find the horizontal angle that from frame-center to merge-contour-center
        horizontal_angle = x_vector * self.horizontal_field_of_view / x_frame_center
        # Find the vertical angle that from frame-center to merge-contour-center
        vertical_angle = y_vector * self.vertical_field_of_view / y_frame_center

        # Find the distance vector from the object (in meters)
        distance_vector = self.focal_length * self.sqrt_object_area / sqrt_cont_area

        # Find the x,y and z distance from the object (in meters)
        rel = np.array([[np.sin(horizontal_angle), np.sin(vertical_angle),
                         np.sqrt(1 - np.sin(horizontal_angle) ** 2 - np.sin(vertical_angle) ** 2)]]) * distance_vector

        # Perform rotation matrix on the distance and add the given offset
        distance = self.rotation_matrix.dot(rel.T).flatten() + self.offset

        data_dictionary['distance_vector_x'] = str(distance[0])
        data_dictionary['distance_vector_y'] = str(distance[1])
        data_dictionary['distance_vector_z'] = str(distance[2])

        logging.info("distance_vector_x " + str(distance[0]))
        logging.info("distance_vector_y " + str(distance[1]))
        logging.info("distance_vector_z " + str(distance[2]))

        return data_dictionary
