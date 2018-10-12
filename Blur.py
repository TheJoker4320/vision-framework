
from IModifier import IModifier
import cv2

class Blur(IModifier):
	
	def __init__(self, kernel):
		self.kernel = kernel

	def modify(pic):

		pic = cv2.GaussianBlur(pic, kernel, 0)		
		return pic 
		