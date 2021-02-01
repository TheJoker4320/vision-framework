from abc import ABCMeta, abstractmethod
from numpy import ndarray


class Filter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def filter(self, contours: [ndarray]) -> [ndarray]:
        """
        :param contours: Contours to go trough the filter
        :type contours: List<contour>

        :rtype: List<contour>
        """
        pass
