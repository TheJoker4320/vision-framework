import json
import cv2
from pipeline.pipeline_factory import PipelineFactory



def main():
	with open("jak.json","r") as f:
		prop = json.load(f)
	factory = PipelineFactory()
	my_pipeline = factory.create_pipeline(prop)
	image = cv2.imread('test.jpg')
	while True:
		my_pipeline.process_image(image)
	


if __name__ == "__main__":
	main()
