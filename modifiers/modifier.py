from abc import ABCMeta, abstractmethod


class Modifier(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def modify(self, picture):
        """
        :param picture: a picture to modify
        :type picture: matrix of pixels
        :rtype: matrix of pixels
        """
        pass
