from abc import ABCMeta, abstractmethod


class IModifier(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def modify(self, pic):
        raise NotImplementedError
