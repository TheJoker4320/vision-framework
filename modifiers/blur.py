from vision_framework.pipeline.pipeline_factory import PipelineFactory
from modifier import Modifier
import cv2


@PipelineFactory.modifier(name="Blur")
class Blur(Modifier):
    """Blurs the image using a kernel."""

    def __init__(self, kernel):
        """
        :param kernel: bluring kernel
        :type kernel: tuple
        """
        self.kernel = kernel

    def modify(self, pic):
        return cv2.GaussianBlur(pic, self.kernel, 0)
