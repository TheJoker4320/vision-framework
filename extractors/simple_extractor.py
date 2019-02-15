from extractor import Extractor
import cv2


class SimpleExtractor(Extractor):
    """extracts all the contours that were detected at the given frame"""

    def extract(self, image):
        return cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
