from abc import ABCMeta, abstractmethod


class ICalculation(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calc(self, contour):
        """
        an abstract function that gets a contour and returns a dictionary with
        calculated data
        """
        pass
