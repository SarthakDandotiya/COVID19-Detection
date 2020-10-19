
from tensorflow.keras.models import load_model
from tensorflow.keras.models import model_from_json

import cv2
import numpy as np
import argparse
import logging
import os


def detection(path):
    print("[INFO] Evaluating network...")

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
    logging.getLogger('tensorflow').setLevel(logging.FATAL)

    model_architecture = 'architecture.json'
    model_weights = 'weights.h5'

    print("[INFO] Loading Model & Weights...")
    json_file = open('architecture.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights("weights.h5")

    print("[INFO] Resizing input image...")
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))

    predIdxs = model.predict(np.array([img, ])/255.0, batch_size=1)[0]

    print("[INFO] Done...\n\n")

    if predIdxs[0] > predIdxs[1]:
        return 1
    else:
        return -1
