from extractors.extractor import Extractor
from numpy import ndarray
import cv2


class SimpleExtractor(Extractor):
    """
    Extracts all the contours that were detected at the given frame
    """

    def extract(self, frame: ndarray) -> [ndarray]:
        return cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[1]
