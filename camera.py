import os
import cv2


class Camera:

    def __init__(self, port):
        """

        :param int port: the port that the camera connect too
        """
        self.port = port
        self.init_string_port = str(self.port)

    def configure_brightness(self, brightness):
        """

        configure the brightness
        :param brightness: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c brightness=" + str(brightness))

    def configure_contrast(self, contrast):
        """

        configure the contrast
        :param contrast: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c contrast=" + str(contrast))

    def configure_saturation(self, saturation):
        """

        configure the saturation
        :param saturation: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c saturation=" + str(saturation))

    def configure_white_balance_temperature_auto(self, white_balance_temperature_auto):
        """

        configure the auto white balance temperature
        :param white_balance_temperature_auto: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c white_balance_temperature_auto=" + str(
            white_balance_temperature_auto))

    def configure_power_line_frequency(self, power_line_frequency):
        """

        configure the power line frequency
        :param power_line_frequency: int
        """
        os.system(
            "v4l2-ctl -d /dev/video" + self.init_string_port + " -c power_line_frequency=" + str(power_line_frequency))

    def configure_white_balance_temperature(self, white_balance_temperature):
        """

        configure the white balance temperature
        :param white_balance_temperature: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c white_balance_temperature=" + str(
            white_balance_temperature))

    def configure_sharpness(self, sharpness):
        """

        configure the sharpness
        :param sharpness: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c sharpness=" + str(sharpness))

    def configure_backlight_compensation(self, backlight_compensation):
        """

        configure the backlight compensation
        :param backlight_compensation: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c backlight_compensation=" + str(
            backlight_compensation))

    def configure_exposure_auto(self, exposure_auto):
        """

        configure the auto exposure
        :param exposure_auto: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c exposure_auto=" + str(exposure_auto))

    def configure_exposure_absolute(self, exposure_absolute):
        """

        configure the absolute exposure
        :param exposure_absolute: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c exposure_absolute=" + str(exposure_absolute))

    def configure_pan_absolute(self, pan_absolute):
        """

        configure the absolute pan
        :param pan_absolute: int
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c pan_absolute=" + str(pan_absolute))

    def configure_tilt_absolute(self, tilt_absolute):
        """

        configure the absolute tilt
        :param tilt_absolute:
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c tilt_absolute=" + str(tilt_absolute))

    def configure_zoom_absolute(self, zoom_absolute):
        """

        configure the absolute zoom
        :param zoom_absolute:
        """
        os.system("v4l2-ctl -d /dev/video" + self.init_string_port + " -c zoom_absolute=" + str(zoom_absolute))

    def get_frame(self):
        """

        :return: an adjust frame
        """
        video_capture = cv2.VideoCapture(self.port)
        _, image = video_capture.read()
        return image
