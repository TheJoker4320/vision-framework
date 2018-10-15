from abc import ABCMeta, abstractmethod


class IModifier(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def modify(self, picture):
        """

        :rtype: picture
        :param picture:
        :type picture:
        """
