from abc import ABCMeta, abstractmethod


class IPublish(object):
    __metaclass__ = ABCMeta

    """ an abstract function that gets a dictionary and sends it to the robot """
    @abstractmethod
    def publish(self, dict):
        pass
