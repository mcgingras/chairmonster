import os, cv2, keras
import numpy as np
from keras.models import load_model

def classify(im):
    im_keras = im.reshape(1, 28, 28, 1)
    keras_result = keras_model.predict(im_keras)[0]
    if keras_result[1] > keras_result[0]:
        return "chair"
    else:
        return "sofa"

def process(im):
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im_final = cv2.resize(im_gray, (28, 28))

    return im_final

class Classifier():
    def __init__(self):
        pass

    def predict(self):
        imagePath = "/Users/mcgingras/IDEO/Summer18/Build/Boston/chairs/data/sketch.png"
        image = cv2.imread(imagePath)
        im_process = process(image)
        result = classify(im_process)
        return result



if __name__ == '__main__':
    keras_model = load_model('/Users/mcgingras/IDEO/Summer18/Build/Boston/chairs/python/analysis/model_keras.h5')
    c = Classifier()
    print(c.predict())
