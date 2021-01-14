import logging
from publishers.publish import Publish


class LoggingPublisher(Publish):
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
        for key, value in data_dict.items():
            logging.info("{key}:{value}".format(key=key, value=value))
