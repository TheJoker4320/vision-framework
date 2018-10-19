from ICalculation import ICalculation
import cv2
import  math

class AngleCalculation(ICalculation):
    """
    Calculate the x and y angels between the camara and the object in the image
    """
    def __init__(self, focal_length):
        self.focal_length = focal_length

    def calc(self,IMAGE_X_CENTER,IMAGE_Y_CENTER):
        x_center, y_center = self._find_point()
        x_angle = math.atan((x_center - IMAGE_X_CENTER) / self.focal_length)
        x_angle = math.degrees(x_angle)
        y_angle = math.atan((y_center - IMAGE_Y_CENTER) / self.focal_length)
        y_angle = math.degrees(y_angle)
        return x_angle, y_angle