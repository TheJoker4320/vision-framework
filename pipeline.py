import cv2
import logging


class Pipeline(object):
    """
        represents a single pipeline
        responsible for processing image via modifiers, filters, calculations and
         publishers
    """

    def __init__(self, modifiers, filters, calculations, publishers):
        """

        :param modifiers: the modifiers that the frame will pass trough
        :type modifiers: list<IModifier>
        :param filters: the filters that the contours which was detected in the
         frame will pass trough
        :type filters: list<IFilter>
        :param calculations: the calculations that will be enabled on the
        contours
        :type calculations: list<ICalculation>
        :param publishers: different ways to publish the results of the
        calculations
        :type publishers: list<IPublishers>
        """
        self.modifiers = modifiers
        self.filters = filters
        self.calculations = calculations
        self.publishers = publishers

    def process_image(self, frame):
        """

        :param frame: a frame from the camera
        :type frame: two dimensional array of pixels
        """
        for modifier in self.modifiers:
            frame = modifier.modify(frame)

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, contours, _ = cv2.findContours(gray_frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        if len(contours) == 0:
            return

        for filter_object in self.filters:
            contours = filter_object.filter(contours)

        Pipeline.__check_contours(contours)
        if len(contours) == 0:
            return
        contour = contours[0]  # the first contour that passed all filters
        """
        this iteration responsible for publishing via different publishers
        the results of the calculations
        """
        for calculation in self.calculations:
            for publisher in self.publishers:
                publisher.publish(calculation.calc(contour))

    @staticmethod
    def __check_contours(contours):
        """logs the status of the contour's quantity"""
        contour_counter = len(contours)
        if contour_counter == 0:
            logging.info("there were not found any counter")
        elif contour_counter == 1:
            logging.info("single contour was found")
        logging.info("multiple contours were found")
