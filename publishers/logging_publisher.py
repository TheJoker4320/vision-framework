import logging
from publish import Publish


class Logging_publisher(Publish):  # Consider Changing the name of the class
    """
    A publish class
    Responsible for logging the information at info level
    """

    def publish(self, data_dict):
        """
        WIP
        :param data_dict:
        :return:
        """
        for key, value in data_dict.iteritems():
            logging.info("{key}:{value}".format(key=key, value=value))
