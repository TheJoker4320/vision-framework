import json
import logging
import collections

from camera import Camera
from pipeline.pipeline_factory import PipelineFactory
from networktables import NetworkTables
from remote_tuner import RemoteTuner


def main():
    logging.basicConfig(level=logging.INFO)

    with open("examples/example.json", "r") as file_handler:
        properties = json.load(file_handler, object_pairs_hook=collections.OrderedDict)
    print properties
    my_pipeline = PipelineFactory.create_pipeline(properties)

    camera_settings = properties['camera settings']
    camera = Camera(camera_settings['id'])
    camera.set_camera_settings(camera_settings)
    NetworkTables.initialize(server='127.0.0.1')
    r = RemoteTuner("examples/example.json",my_pipeline)
    while True:
        frame = camera.get_frame()
        my_pipeline.process_image(frame)
        my_pipeline = r.get_pipeline()

if __name__ == "__main__":
    main()
