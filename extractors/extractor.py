from abc import ABCMeta, abstractmethod


class Extractor(object):
    """
    The class responsible for extracting contours from image
    The image needs to be a gray image
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def extract(self, image):
        """
        :param image: An image to extract contours from
        :type image: numpy array
        :return: extracted contours from the image
        :rtype: List<contour>
        """
        pass
