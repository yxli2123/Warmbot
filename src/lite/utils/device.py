import cv2
from gpiozero import DistanceSensor


class Camera:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        assert self.cap.isOpened(), "Camera is not available"

    def capture_frame(self, gray=True):
        ret, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY if gray else cv2.COLOR_BGR2RGB)
        return frame

