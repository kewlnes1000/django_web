import numpy as np
import dlib
import cv2

#取得預設的臉部偵測器
detector = dlib.get_frontal_face_detector()
#根據shape_predictor方法載入68個特徵點模型，此方法為人臉表情識別的偵測器
predictor = dlib.shape_predictor( 'shape_predictor_68_face_landmarks.dat')
  
class FaceRecognition():
  def readImage(self, blob):
    img = cv2.imread(blob)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)