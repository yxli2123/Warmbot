from gpiozero import DistanceSensor
from utils.device import Camera
from utils.emotion_detection import EmotionDetection


def wait_for_start(threshold_distance=0.5):
    sensor = DistanceSensor(echo=18, trigger=14, max_distance=2)
    while True:
        if sensor.distance < threshold_distance:
            break


def main():
    wait_for_start()

    # Initialize devices
    camera = Camera()
    detection = EmotionDetection()

    # 1. Detect facial emotion
    frame = camera.capture_frame(gray=True)
    emotion = detection.recognize(frame)  # "neutral | happiness | surprise | sadness | anger | disgust | fear"
    print(f"You look {emotion} today. What's going on?")

    # TODO: Play sound and video

    # 2. Talk with the user
    # TODO: Talk Agent


if __name__ == '__main__':
    main()
