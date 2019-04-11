import numpy as np
import dlib
import cv2
import base64
import os


face_shape_path = "{base_path}\shape_predictor_68_face_landmarks.dat".format(
	base_path=os.path.abspath(os.path.dirname(__file__)))

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor(face_shape_path)
  
class FaceRecognition():

  def readImage(blob):
    
    nparr = np.fromstring(blob, np.uint8)

    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    face_rects, scores, idx = detector.run(frame, 0)
    
    for i, d in enumerate(face_rects):
      x1 = d.left()
      y1 = d.top()
      x2 = d.right()
      y2 = d.bottom()
      
      cv2.rectangle(frame, (x1, y1), (x2, y2), ( 0, 0, 255), 2, cv2. LINE_AA)
 
      landmarks_frame = cv2.cvtColor(frame, cv2. COLOR_BGR2RGB)

      shape = predictor(landmarks_frame, d)
 
      for i in range( 68):
        cv2.circle(frame,(shape.part(i).x,shape.part(i).y), 1,( 0, 255, 255), -1)

    frame_str = cv2.imencode('.jpg', frame)[1].tostring()
    
    return frame_str
    