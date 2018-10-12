import cv2
from IFilter import IFilter 
    
class AreaRangeFilter(IFilter):

	def __init__(self, MIN_AREA, MAX_AREA):
		self.MIN_AREA = MIN_AREA
		self.MAX_AREA = MAX_AREA
	
	def filter(self,contours):
		new_cnt = []
		for cnt in contours:
			area = cv2.countourArea(cnt)
			if MIN_AREA <= area <= MAX_AREA:
				new_cnt.append(cnt)
		return new_cnt