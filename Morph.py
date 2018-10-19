from IModifier import IModifier
import cv2

"""Gets a frame and applies morphology to it """
class Morph(IModifier):

    def __init__(self, morph_open=None, morph_close=None, use_open=None, use_close=None):
        self.morph_open = morph_open
        self.morph_close = morph_close
        self.use_open = use_open
        self.use_close = use_close

    def modify(self, frame):
        if self.use_open:
            frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, self.morph_open)
        if self.use_close:
            frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, self.morph_close)
        return frame
