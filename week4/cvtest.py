
import numpy as np
import urllib3
import cv2
 
url = 'http://www.pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png'
http = urllib3.PoolManager()
r = http.request('GET',url)
print(r)
image = np.asarray(bytearray(r.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)
cv2.imshow('URL2Image',image)