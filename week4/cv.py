import numpy as np
import dlib
import cv2
import base64

#取得預設的臉部偵測器
# detector = dlib.get_frontal_face_detector()
#根據shape_predictor方法載入68個特徵點模型，此方法為人臉表情識別的偵測器
# predictor = dlib.shape_predictor( 'shape_predictor_68_face_landmarks.dat')
  
class FaceRecognition():
  def readImage(blob):
    # print(type(blob))
    nparr = np.fromstring(blob, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img_g = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # print(type(img))
    img_str = cv2.imencode('.jpg', img_g)[1].tostring()
    # print(img_str)
    return img_str
    # img = cv2.imread(blob)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)