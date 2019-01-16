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

        logging.debug("post modifying")
        if not Pipeline.__contain_contour(contours):
            return

        for filter_object in self.filters:
            contours = filter_object.filter(contours)
            logging.debug("{} passed {}".format(len(contours), type(filter_object).__name__))

        logging.debug("post filtering")
        if not Pipeline.__contain_contour(contours):
            return
        contour = contours[0]
        """
        this iteration responsible for publishing via different publishers
        the results of the calculations
        """
        for calculation in self.calculations:
            calc = calculation.calc(contour)
            for publisher in self.publishers:
                publisher.publish(calc)

    @staticmethod
    def __contain_contour(contours):
        """
        logs the status of the contour's quantity
        return if the amount of contours greater than 0
        """
        contour_amount = len(contours)
        if contour_amount == 0:
            logging.warning("there were not found any counter")
            return False
        elif contour_amount == 1:
            logging.debug("single contour was found")
        logging.debug("multiple contours were found")
        return True
