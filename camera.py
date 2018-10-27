import os


class Camera:

    def __init__(self, cv2, port):
        """

        :param opencv cv2: parameter from type library
        :param int port: the port that the camera connect too
        """
        self.cv2 = cv2
        self.port = port

    def get_port(self):
        """

        :return: the port that the camera connect to
        """
        return self.port

    def set_port(self, port):
        """

        set the port of the camera
        :param port: int
        """
        self.port = port

    @staticmethod
    def configure_brightness(brightness):
        """

        configure the brightness
        :param brightness: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c brightness=" + str(brightness))

    @staticmethod
    def configure_contrast(contrast):
        """

        configure the contrast
        :param contrast: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c contrast=" + str(contrast))

    @staticmethod
    def configure_saturation(saturation):
        """

        configure the saturation
        :param saturation: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c saturation=" + str(saturation))

    @staticmethod
    def configure_white_balance_temperature_auto(white_balance_temperature_auto):
        """

        configure the auto white balance temperature
        :param white_balance_temperature_auto: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c white_balance_temperature_auto=" + str(white_balance_temperature_auto))

    @staticmethod
    def configure_power_line_frequency(power_line_frequency):
        """

        configure the power line frequency
        :param power_line_frequency: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c power_line_frequency=" + str(power_line_frequency))

    @staticmethod
    def configure_white_balance_temperature(white_balance_temperature):
        """

        configure the white balance temperature
        :param white_balance_temperature: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c white_balance_temperature=" + str(white_balance_temperature))

    @staticmethod
    def configure_sharpness(sharpness):
        """

        configure the sharpness
        :param sharpness: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c sharpness=" + str(sharpness))

    @staticmethod
    def configure_backlight_compensation(backlight_compensation):
        """

        configure the backlight compensation
        :param backlight_compensation: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c backlight_compensation=" + str(backlight_compensation))

    @staticmethod
    def configure_exposure_auto(exposure_auto):
        """

        configure the auto exposure
        :param exposure_auto: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c exposure_auto=" + str(exposure_auto))

    @staticmethod
    def configure_exposure_absolute(exposure_absolute):
        """

        configure the absolute exposure
        :param exposure_absolute: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c exposure_absolute=" + str(exposure_absolute))

    @staticmethod
    def configure_pan_absolute(pan_absolute):
        """

        configure the absolute pan
        :param pan_absolute: int
        """
        os.system("v4l2-ctl -d /dev/video1 -c pan_absolute=" + str(pan_absolute))

    @staticmethod
    def configure_tilt_absolute(tilt_absolute):
        """

        configure the absolute tilt
        :param tilt_absolute:
        """
        os.system("v4l2-ctl -d /dev/video1 -c tilt_absolute=" + str(tilt_absolute))

    @staticmethod
    def configure_zoom_absolute(zoom_absolute):
        """

        configure the absolute zoom
        :param zoom_absolute:
        """
        os.system("v4l2-ctl -d /dev/video1 -c zoom_absolute=" + str(zoom_absolute))

    def get_frame(self):
        """

        :return: an adjust frame
        """
        video_capture = self.cv2.VideoCapture(self.port)
        success, image = video_capture.read()
        return image
