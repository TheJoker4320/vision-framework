import logging
from publish import Publish


class Logging_publisher(Publish):
    """
    A publish class
    Responsible for logging the information at info level
    """

    def publish(self, data_dict):
        for key, value in data_dict.iteritems():
            logging.info("{key}:{value}".format(key=key, value=value))
