import json
from pipeline.pipeline_factory import PipelineFactory
import logging
from camera import Camera
import cv2


def main():
    logging.basicConfig(level=logging.INFO)
    # cv2.namedWindow("screen1")
    # cv2.namedWindow("screen2")

    with open("properties.json", "r") as file_handler:
        properties = json.load(file_handler)
    my_pipeline = PipelineFactory.create_pipeline(properties)

    camera_settings = properties['camera settings']
    camera = Camera(camera_settings['id'])
    camera.camera_setting_setter(camera_settings)
    while True:
        frame = camera.get_frame()
        # cv2.imshow('screen1',frame)
        my_pipeline.process_image(frame)


if __name__ == "__main__":
    main()
