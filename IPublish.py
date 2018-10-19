from abc import ABCMeta, abstractmethod


class IPublish(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def publish(self, data_dict):
        """
        :param data:
        :type data:
        """
        pass
