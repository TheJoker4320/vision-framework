import json
import logging
import cv2
import collections

from threading import Thread
from streamer import Streamer
from camera import Camera

from pipeline.pipeline_factory import PipelineFactory
from networktables import NetworkTables


def main():
    logging.basicConfig(level=logging.INFO)

    with open("examples/example.json", "r") as file_handler:
        properties = json.load(file_handler, object_pairs_hook=collections.OrderedDict)
    my_pipeline = PipelineFactory.create_pipeline(properties)
    
    camera_settings = properties['camera settings']
    camera = Camera(camera_settings['id'], cv2.CAP_V4L)
    #camera.set_camera_settings(camera_settings)
    
    NetworkTables.initialize(server='10.43.20.69')
    # frame = cv2.imread('ball.jpg')
    
    # frame = cv2.imread('diagonal_test.jpg')
    
    while True:
        frame = camera.get_frame()
        processed_frame = my_pipeline.process_image(frame)

    
if __name__ == "__main__":
    main()
