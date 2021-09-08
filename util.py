import joblib
import json
import numpy as np
import base64
import cv2
from wavelet import w2d

__class_name_to_number = {}
__class_number_to_name = {}

__model = None

def class_number_to_name(class_num):
    return __class_number_to_name[class_num]

