from abc import ABCMeta, abstractmethod


class Filter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def filter(self, contours):
        """
        :rtype: List<contour>
        :param contours: contours to go trough the filter
        :type contours: List<contour>
        """
        pass
