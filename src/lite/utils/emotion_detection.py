import cv2
from PIL import Image
import torch
import torch.nn as nn
import torchvision.transforms as transforms


class FaceEmotionCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.cnn1 = nn.Conv2d(1, 8, 3)
        self.cnn2 = nn.Conv2d(8, 16, 3)
        self.cnn3 = nn.Conv2d(16, 32, 3)
        self.cnn4 = nn.Conv2d(32, 64, 3)
        self.cnn5 = nn.Conv2d(64, 128, 3)
        self.cnn6 = nn.Conv2d(128, 256, 3)
        self.cnn7 = nn.Conv2d(256, 256, 3)
        self.relu = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2, 1)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.cnn1_bn = nn.BatchNorm2d(8)
        self.cnn2_bn = nn.BatchNorm2d(16)
        self.cnn3_bn = nn.BatchNorm2d(32)
        self.cnn4_bn = nn.BatchNorm2d(64)
        self.cnn5_bn = nn.BatchNorm2d(128)
        self.cnn6_bn = nn.BatchNorm2d(256)
        self.cnn7_bn = nn.BatchNorm2d(256)
        self.fc1 = nn.Linear(1024, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 7)
        self.dropout = nn.Dropout(0.3)
        self.log_softmax = nn.LogSoftmax(dim=1)

    def forward(self, x):
        x = self.relu(self.pool1(self.cnn1_bn(self.cnn1(x))))
        x = self.relu(self.pool1(self.cnn2_bn(self.dropout(self.cnn2(x)))))
        x = self.relu(self.pool1(self.cnn3_bn(self.cnn3(x))))
        x = self.relu(self.pool1(self.cnn4_bn(self.dropout(self.cnn4(x)))))
        x = self.relu(self.pool2(self.cnn5_bn(self.cnn5(x))))
        x = self.relu(self.pool2(self.cnn6_bn(self.dropout(self.cnn6(x)))))
        x = self.relu(self.pool2(self.cnn7_bn(self.dropout(self.cnn7(x)))))

        x = x.view(x.size(0), -1)

        x = self.relu(self.dropout(self.fc1(x)))
        x = self.relu(self.dropout(self.fc2(x)))
        x = self.log_softmax(self.fc3(x))
        return x

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)


class EmotionDetection:
    def __init__(self,
                 model_path='./data/FER_trained_model.pt',
                 face_detect_file_path='./data/haarcascade_frontalface_default.xml'):

        # load model for emotion recognition
        self.model = FaceEmotionCNN()
        self.model.load_state_dict(torch.load(model_path, map_location=lambda storage, loc: storage), strict=False)
        self.model = self.model.cpu()
        self.model.eval()

        # load model for face detection
        self.face_cascade = cv2.CascadeClassifier(face_detect_file_path)

        # others
        self.transform = transforms.ToTensor()
        self.emotion_dict = {0: 'neutral', 1: 'happiness', 2: 'surprise', 3: 'sadness',
                             4: 'anger', 5: 'disgust', 6: 'fear'}

    def recognize(self, raw_frame):
        """
        :param raw_frame: frame captured by camera, not cropped to face
        :return: emotion class of the face
        """
        faces = self.face_cascade.detectMultiScale(raw_frame)
        for (x, y, w, h) in faces:
            face_img = cv2.resize(raw_frame[y:y + h, x:x + w], (48, 48))
            face_img = face_img / 255.0
            face_img = Image.fromarray(face_img)
            face_img = self.transform(face_img).unsqueeze(0)
            with torch.no_grad():
                logits = self.model(face_img).squeeze()
                emotion = logits.argmax()
                emotion = self.emotion_dict[emotion.item()]
                return emotion  # may have many faces, but only return the emotion of the first face
