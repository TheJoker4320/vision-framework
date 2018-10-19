from abc import ABCMeta, abstractmethod


class IFilter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def filter(self, contours):
        """

        :rtype: contours
        :param contours:
        :type contours:
        """
        pass
