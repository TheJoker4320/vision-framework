from abc import ABCMeta, abstractmethod


class IPublish(object):
    __metaclass__ = ABCMeta

    """ An abstract function that gets a data dictionary and publish its data """
    @abstractmethod
    def publish(self, data_dict):
        pass
