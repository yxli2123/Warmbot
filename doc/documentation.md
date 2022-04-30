# Documentation for Warmbot

## 1. Overview

Inputs:

- An **infrared sensor** on neck or belly
- 2 **gas pressure sensors** on each arm
- 2 **microphones** in each ear
- [option] A **camera** on the head

Outputs:

- A **screen** on the face
- 2 **speakers** on each side of the face

Processor:

- A Raspberry PI 4

## 2. Functions

**Start**

- Start when a user approaches [infrared sensor]

- Start when a user push the hard button [button]

**Active Interation**

- Detect the user's emotion [camera]  ----> Talk to the user [speaker]

**Passive Interaction**

- Listen to the user [microphone] ----> Give feedbacks [speaker]
- Measure arm pressure [pressure sensor] ----> Give feedbacks [screen]

## 3. Implementation

```
.
└── Warmrobot/
    ├── device/
    │   ├── ultrasonic_sensor
    │   ├── pressure_sensor
    │   ├── camera
    │   ├── speaker
    │   ├── microphone
    │   └── screen
    ├── utils/
    │   ├── speech-to-text
    │   ├── text-to-speech
    │   ├── emotion-detection
    │   └── ...
    ├── interaction/
    │   ├── start
    │   ├── talk
    │   ├── listen
    │   ├── play
    │   └── end
    └── main

```



### 3.1 Low-level functions

```python
def detect_pressure(device=pressure_sensor, when='active', IO='GPIO_1'):
    """
    pressure sensor --> voltage --ADC--> pressure value
    require Raspberry PI packages to receive data from GPIO
    """
    return pressure

def detect_emotion(device=camera, time='always', IO='USB'):
    """
    realtime frames --DNN--> emotion classes
    require tensorflow packages
    """
    return emotion

def listen(device=microphone, time='active', IO='USB'):
    """
    speech --speech-to-text--> text
    require speech to text 
    """

```





