import os
import cv2


class Camera(object):
    """
    An camera class
    Has option to set configuration
    """

    TEMPLATE = "v4l2-ctl -d /dev/video"
    configuration_strings = [
        "brightness",
        "contrast",
        "saturation",
        "white_balance_temperature_auto",
        "power_line_frequency",
        "white_balance_temperature",
        "sharpness",
        "backlight_compensation",
        "exposure_auto",
        "exposure_absolute",
        "pan_absolute",
        "tilt_absolute",
        "zoom_absolute"
    ]

    def __init__(self, port):
        """
        :param int port: the port that the camera connect too
        """
        port = int(port)
        self.video_capture = cv2.VideoCapture(port)
        self.initial_string = "{template}{port}".format(template=Camera.TEMPLATE, port=port)

    def config(self, configuration, value):
        """
        configure the configuration with the value
        :param configuration: string
        :param value: int
         """
        os.system("{initial_string} -c {configuration}={value}".format(initial_string=self.initial_string,
                                                                       configuration=configuration,
                                                                       value=value))

    def set_camera_settings(self, properties):
        """
        Sets camera configurations by a given set of properties
        The properties need to be registered
        Use configuration decorator to register setting functions
        :param properties: the properties of the camera to apply on
        :type properties: dictionary
        """
        for key, value in properties.iteritems():
            if key in Camera.configuration_strings:
                self.config(key, value)

    def get_frame(self):
        """
        :return: An adjust frame
        """

        _, image = self.video_capture.read()
        return image
