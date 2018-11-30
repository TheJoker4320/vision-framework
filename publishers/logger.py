import logging
from publish import Publish


class Logger(Publish):
    def publish(self, data_dict):
        for key, value in data.iteritems():
            logging.info("{key}:{value}".format(key=key, value=value))
