import json
from pipeline.pipeline_factory import PipelineFactory
import logging
from camera import Camera


def main():
    logging.basicConfig(filename='logger.log', level=logging.INFO)

    with open("properties.json", "r") as file_handler:
        properties = json.load(file_handler)
    my_pipeline = PipelineFactory.create_pipeline(properties)

    camera_settings = properties['camera settings']
    camera = Camera(camera_settings['id'])
    Camera.camera_setting_setter(camera_settings)
    while True:
        my_pipeline.process_image(camera.get_frame())


if __name__ == "__main__":
    main()
