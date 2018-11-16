from IModifier import IModifier
import cv2


class Morph(IModifier):
    """
    gets a frame and applies open or close or both open and close
    or none of them and returns the modified frame
    """

    def __init__(self, morph_open, morph_close):
        self.morph_open = morph_open
        self.morph_close = morph_close

    def modify(self, frame):
        modified_frame = frame
        if self.morph_open != 0:
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, self.morph_open)
        if self.morph_open != 0:
            modified_frame = cv2.morphologyEx(frame, cv2.MORPH_CLOSE, self.morph_close)
        return modified_frame
