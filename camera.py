import os
import cv2


class Camera:
    template = "v4l2-ctl -d /dev/video"
    configuration_functions = {}

    def __init__(self, port):
        """

        :param int port: the port that the camera connect too
        """
        self.port = port
        self.initial_string = Camera.template + str(self.port)

    @staticmethod
    def configuration(configure):
        # A function decorator that registers the function in the configuration dictionary

        def decorator_function(func):
            Camera.configuration_functions[configure] = func
            return func

        return decorator_function

    def config(self, configuration, value):
        """
        configure the configuration with the value
        :param configuration: string
        :param value: int
         """
        os.system("{initial_string} -c {configuration}={value}".format(initial_string=self.initial_string,
                                                                       configuration=configuration,
                                                                       value=value))

    @configuration(configure="brightness")
    def configure_brightness(self, brightness):
        """
        configure the brightness
        :param brightness: int
        """
        self.config(Camera.configuration_strings["brightness_string"], brightness)

    @configuration(configure="contrast")
    def configure_contrast(self, contrast):
        """
        configure the contrast
        :param contrast: int
        """
        self.config(Camera.contrast_string, contrast)

    @configuration(configure="saturation")
    def configure_saturation(self, saturation):
        """
        configure the saturation
        :param saturation: int
        """
        self.config(Camera.saturation_string, saturation)

    @configuration(configure="white_balance_temperature_auto")
    def configure_white_balance_temperature_auto(self, white_balance_temperature_auto):
        """
        configure the auto white balance temperature
        :param white_balance_temperature_auto: int
        """
        self.config(Camera.white_balance_temperature_auto_string, white_balance_temperature_auto)

    @configuration(configure="power_line_frequency")
    def configure_power_line_frequency(self, power_line_frequency):
        """
        configure the power line frequency
        :param power_line_frequency: int
        """
        self.config(Camera.power_line_frequency_string, power_line_frequency)

    @configuration(configure="white_balance_temperature")
    def configure_white_balance_temperature(self, white_balance_temperature):
        """
        configure the white balance temperature
        :param white_balance_temperature: int
        """
        self.config(Camera.white_balance_temperature_string, white_balance_temperature)

    @configuration(configure="sharpness")
    def configure_sharpness(self, sharpness):
        """
        configure the sharpness
        :param sharpness: int
        """
        self.config(Camera.sharpness_string, sharpness)

    @configuration(configure="backlight_compensation")
    def configure_backlight_compensation(self, backlight_compensation):
        """
        configure the backlight compensation
        :param backlight_compensation: int
        """
        self.config(Camera.backlight_compensation_string, backlight_compensation)

    @configuration(configure="exposure_auto")
    def configure_exposure_auto(self, exposure_auto):
        """
        configure the auto exposure
        :param exposure_auto: int
        """
        self.config(Camera.exposure_auto_string, exposure_auto)

    @configuration(configure="exposure_absolute")
    def configure_exposure_absolute(self, exposure_absolute):
        """
        configure the absolute exposure
        :param exposure_absolute: int
        """
        self.config(Camera.exposure_absolute_string, exposure_absolute)

    @configuration(configure="pan_absolute")
    def configure_pan_absolute(self, pan_absolute):
        """
        configure the absolute pan
        :param pan_absolute: int
        """
        self.config(Camera.pan_absolute_string, pan_absolute)

    @configuration(configure="tilt_absolute")
    def configure_tilt_absolute(self, tilt_absolute):
        """
        configure the absolute tilt
        :param tilt_absolute:
        """
        self.config(Camera.tilt_absolute_string, tilt_absolute)

    @configuration(configure="zoom_absolute")
    def configure_zoom_absolute(self, zoom_absolute):
        """
        configure the absolute zoom
        :param zoom_absolute:
        """
        self.config(Camera.zoom_absolute_string, zoom_absolute)

    def get_frame(self):
        """

        :return: an adjust frame
        """
        video_capture = cv2.VideoCapture(self.port)
        _, image = video_capture.read()
        return image
