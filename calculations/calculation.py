from abc import ABCMeta, abstractmethod
from numpy import ndarray


class Calculation(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calc(self, contours: [ndarray]) -> dict:
        """
        :param contours: The relevant contours (the ones that passed the filter and can be used for the calculations)
        :type contours: List<contour>

        :rtype: dict
        """
        pass
