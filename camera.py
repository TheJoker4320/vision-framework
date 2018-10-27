import os


class Camera:

    def __init__(self, cv2, port):
        self.cv2 = cv2
        self.port = port

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    @staticmethod
    def configure_brightness(brightness):
        os.system("v4l2-ctl -d /dev/video1 -c brightness=" + str(brightness))

    @staticmethod
    def configure_contrast(contrast):
        os.system("v4l2-ctl -d /dev/video1 -c contrast=" + str(contrast))

    @staticmethod
    def configure_saturation(saturation):
        os.system("v4l2-ctl -d /dev/video1 -c saturation=" + str(saturation))

    @staticmethod
    def configure_white_balance_temperature_auto(white_balance_temperature_auto):
        os.system("v4l2-ctl -d /dev/video1 -c white_balance_temperature_auto=" + str(white_balance_temperature_auto))

    @staticmethod
    def configure_power_line_frequency(power_line_frequency):
        os.system("v4l2-ctl -d /dev/video1 -c power_line_frequency=" + str(power_line_frequency))

    @staticmethod
    def configure_white_balance_temperature(white_balance_temperature):
        os.system("v4l2-ctl -d /dev/video1 -c white_balance_temperature=" + str(white_balance_temperature))

    @staticmethod
    def configure_sharpness(sharpness):
        os.system("v4l2-ctl -d /dev/video1 -c sharpness=" + str(sharpness))

    @staticmethod
    def configure_backlight_compensation(backlight_compensation):
        os.system("v4l2-ctl -d /dev/video1 -c backlight_compensation=" + str(backlight_compensation))

    @staticmethod
    def configure_exposure_auto(exposure_auto):
        os.system("v4l2-ctl -d /dev/video1 -c exposure_auto=" + str(exposure_auto))

    @staticmethod
    def configure_exposure_absolute(exposure_absolute):
        os.system("v4l2-ctl -d /dev/video1 -c exposure_absolute=" + str(exposure_absolute))

    @staticmethod
    def configure_pan_absolute(pan_absolute):
        os.system("v4l2-ctl -d /dev/video1 -c pan_absolute=" + str(pan_absolute))

    @staticmethod
    def configure_tilt_absolute(tilt_absolute):
        os.system("v4l2-ctl -d /dev/video1 -c tilt_absolute=" + str(tilt_absolute))

    @staticmethod
    def configure_zoom_absolute(zoom_absolute):
        os.system("v4l2-ctl -d /dev/video1 -c zoom_absolute=" + str(zoom_absolute))

    def get_frame(self):
        video_capture = self.cv2.VideoCapture(1)
        success, image = video_capture.read()
        return image
