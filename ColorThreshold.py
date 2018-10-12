from IModifier import IModifier
import cv2

class ColorThreshold(IModifier):
	def __init__ (self, low_HSV, high_HSV):
		self.low_HSV = low_HSV
		self.high_HSV = high_HSV

	def modify(self,pic):
		hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)
        	hsv = cv2.inRange(hsv, low_HSV, high_HSV)
		return hsv