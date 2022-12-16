import tensorflow
import cv2
import numpy as np

model_filename_mask = 'models/model_mask.h5'
model_mask = tensorflow.keras.models.load_model(model_filename_mask)

model_filename_string = 'models/model_string.h5'
model_string = tensorflow.keras.models.load_model(model_filename_string)


def preprocessing(frame):
    frame_fliped = cv2.flip(frame, 1)
    size = (224, 224)
    frame_resized = cv2.resize(frame, size, interpolation=cv2.INTER_AREA)
    frame_normalized = (frame_resized.astype(np.float) / 127.0) - 1
    frame_reshaped = frame_normalized.reshape((1, 224, 224, 3))

    return frame_reshaped


capture = cv2.VideoCapture(0)

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)


def predict_mask(frame):
    prediction = model_mask.predict(frame)
    return prediction


def predict_string(frame):
    prediction = model_string.predict(frame)
    return prediction


#마스크 존재 여부
def isExistMask() -> bool:
    "Mask : True     No-Mask : False"
    ret, frame = capture.read()
    preprocessed = preprocessing(frame)
    prediction = predict_mask(preprocessed)

    output = []
    for i in range(2):
        output.append(format(prediction[0, i]*100, ".2f")+"%")

    cv2.putText(frame, "percent:"+str(output), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), thickness=2)
    percent = prediction[0]
    if percent[0] > percent[1]:
        return True  # Mask
    else:
        return False  # No Mask


#마스크 잘림 여부
def isMaskSliced() -> bool:
    "Cut : True     No-Cut : False"
    ret, frame = capture.read()
    preprocessed = preprocessing(frame)
    prediction = predict_string(preprocessed)

    output = []
    for i in range(2):
        output.append(format(prediction[0, i]*100, ".2f")+"%")

    cv2.putText(frame, "percent:"+str(output), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), thickness=2)
    percent = prediction[0]
    if percent[0] < percent[1]:
        return True
    else:
        return False