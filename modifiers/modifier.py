from abc import ABCMeta, abstractmethod
from numpy import ndarray


class Modifier(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def modify(self, frame: ndarray) -> ndarray:
        """
        :param frame: A picture to modify
        :type frame: matrix of pixels (numpy.ndarray)

        :rtype: matrix of pixels (numpy.ndarray)
        """
        pass
