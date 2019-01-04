import json
import logging

from camera import Camera
from pipeline.pipeline_factory import PipelineFactory


def main():
    logging.basicConfig(level=logging.INFO)

    with open("properties.json", "r") as file_handler:
        properties = json.load(file_handler)
    my_pipeline = PipelineFactory.create_pipeline(properties)

    camera_settings = properties['camera settings']
    camera = Camera(camera_settings['id'])
    camera.camera_setting_setter(camera_settings)
    while True:
        frame = camera.get_frame()
        my_pipeline.process_image(frame)


if __name__ == "__main__":
    main()
