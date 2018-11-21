from abc import ABCMeta, abstractmethod


class Calculation(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calc(self, contour):
        
        """
        An abstract function that gets a contour and returns a dictionary with calculated data.
        """
        
        pass
