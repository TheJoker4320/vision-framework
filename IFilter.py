from abc import ABCMeta, abstractmethod


class IFilter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def filter(self, conts):
        raise NotImplementedError
