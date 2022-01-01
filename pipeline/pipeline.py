import cv2
import logging


class Pipeline(object):
    """
    Represents a single pipeline
    Responsible for processing image via modifiers, filters, calculations and publishers
    """

    def __init__(self, modifiers, extractors, filters, calculations, publishers):
        """

        :param modifiers: The modifiers that the frame will pass trough
        :type modifiers: list<IModifier>
        :param extractors: The ways to extract the contours
        :type extractors: list<IExtractor>
        :param filters: The filters that the detected contours in the frame will pass trough
        :type filters: list<IFilter>
        :param calculations: The calculations that will be used on the contours
        :type calculations: list<ICalculation>
        :param publishers: The ways to publish the results of the calculations
        :type publishers: list<IPublishers>
        """
        self.modifiers = modifiers
        self.extractors = extractors
        self.filters = filters
        self.calculations = calculations
        self.publishers = publishers

    def process_image(self, frame):
        """
        :param frame: A frame from the camera
        :type frame: Two dimensional pixel array
        """

        for modifier in self.modifiers:
            frame = modifier.modify(frame)

        contours = []

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        for extractor in self.extractors:
            contours = contours + extractor.extract(gray_frame)

        logging.debug("Modifying stage --------- DONE")
        if not Pipeline.__contain_contour(contours):
            logging.debug("NO CONTOUR FOUND")
            return frame

        for filter_object in self.filters:
            contours = filter_object.filter(contours)
            logging.debug("{} passed {}".format(len(contours), type(filter_object).__name__))

        logging.debug("Filtering stage --------- DONE")
        if not Pipeline.__contain_contour(contours):
            return frame

        cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

        """
        This iteration responsible for publishing (via different publishers)
        the results of the calculations.
        """
        for calculation in self.calculations:
            calc = calculation.calc(contours)
            for publisher in self.publishers:
                publisher.publish(calc)
        return frame

    @staticmethod
    def __contain_contour(contours):
        """
        Logs the status of the contour's quantity
        Returns if the amount of contours is greater than 0
        """
        contour_amount = len(contours)
        if contour_amount == 0:
            logging.warning("there were not found any counter")
            return False
        elif contour_amount == 1:
            logging.debug("single contour was found")
        logging.debug("multiple contours were found")
        return True
