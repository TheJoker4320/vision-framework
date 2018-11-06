from IModifier import IModifier
import cv2

"""Gets a frame and applies morphology to it then returns it"""


class Morph(IModifier):

    def __init__(self, morph_open, morph_close):
        self.morph_open = morph_open
        self.morph_close = morph_close

    def modify(self, frame):
        if self.morph_open != 0:
            frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, self.morph_open)
        if self.morph_open != 0:
            frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, self.morph_close)
        return frame
