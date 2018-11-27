import json
import cv2
from pipeline.pipeline_factory import PipelineFactory
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    with open("jak.json", "r") as f:
        prop = json.load(f)
    my_pipeline = PipelineFactory.create_pipeline(prop)
    image = cv2.imread('test.jpg')
    while True:
        my_pipeline.process_image(image)


if __name__ == "__main__":
    main()
