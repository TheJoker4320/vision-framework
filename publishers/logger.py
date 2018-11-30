import logging
from publish import Publish


class Logger(Publish):
    def publish(self, data_dict):
        for key, value in data_dict.iteritems():
            logging.info("{key}:{value}".format(key=key, value=value))
