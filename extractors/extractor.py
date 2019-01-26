from abc import ABCMeta, abstractmethod


class Extractor(object):
    """
    The class responsible for extracting contours from image
    the image needs to be a gray image
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def extract(self, image):
        """
        :param image: image to extract from it contours
        :type image: numpy array
        :return: extracted contours from the image
        :rtype: List<contour>
        """
        pass
