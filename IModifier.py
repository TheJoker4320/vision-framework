from abc import ABCMeta, abstractmethod


class IModifier(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def modify(self, picture):
        """

        :rtype: matrix of pixels
        :param picture: a picture to modify
        :type picture: matrix of pixels
        """
        pass
