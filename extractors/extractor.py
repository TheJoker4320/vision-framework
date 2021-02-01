from abc import ABCMeta, abstractmethod
from numpy import ndarray


class Extractor(object):
    """
    The class responsible for extracting contours from image
    The image needs to be a gray image
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def extract(self, frame: ndarray) -> [ndarray]:
        """
        :param frame: An image to extract contours from
        :type frame: numpy array

        :return: Extracted contours from the image
        :rtype: List<contour>
        """
        pass
