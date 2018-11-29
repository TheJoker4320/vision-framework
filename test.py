import cv2
from camera import Camera
import time


def main():
    dic = {}
    cam = Camera(1)
    cv2.namedWindow('shit')
    cam.camera_setting_setter(dic)
    # cam.get_frame()
    while True:
	cv2.waitKey(30)    
    	cv2.imshow('shit',cam.get_frame())
	


if __name__ == '__main__':
    main()
