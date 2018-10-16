from abc import ABCMeta, abstractmethod


class IPublish(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def publish(self, network_table):
        raise NotImplementedError