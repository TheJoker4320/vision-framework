from abc import ABCMeta, abstractmethod


class Publish(object):
    """
    an interface which responsible for publishing data
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def publish(self, data_dict):
        """

        :param data_dict: the dictionary to publish
        :type data_dict: dictionary
        """
        pass
