from abc import ABCMeta, abstractmethod

class ICalculation(object):
    __metaclass__ = ABCMeta

    """ an abstract function that gets a contours and sends a dictionary """
    @abstractmethod
    def calc(self, cnt):
        pass
