from abc import ABCMeta, abstractmethod


class Publish(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def publish(self, data_dict):
        """
        :param data_dict: The dictionary to publish
        :type data_dict: dictionary
        """
        pass
