import cv2
from camera import Camera


def main():
    dic = {}
    cv2.namedWindow('shit')
    cap = cv2.VideoCapture(0)
    cam = Camera(0)
    cam.camera_setting_setter(dic)
    while True:
        _, frame = cap.read()
        cv2.imshow('shit', frame)


if __name__ == '__main__':
    main()
