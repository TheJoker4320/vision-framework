import json
import logging
import collections
from threading import Thread
from streamer import Streamer

from camera import Camera
from pipeline.pipeline_factory import PipelineFactory
import cv2


def main():
    logging.basicConfig(level=logging.INFO)

    with open("examples/example.json", "r") as file_handler:
        properties = json.load(file_handler, object_pairs_hook=collections.OrderedDict)
    my_pipeline = PipelineFactory.create_pipeline(properties)

    camera_settings = properties['camera settings']
    camera = Camera(camera_settings['id'])
    camera.set_camera_settings(camera_settings)

    feed = Streamer()

    Thread(target=feed.run).start()
    # frame = cv2.imread('diagonal_test.jpg')
    while True:
        frame = camera.get_frame()
        processed_frame = my_pipeline.process_image(frame)
        feed.update(processed_frame)


if __name__ == "__main__":
    main()
