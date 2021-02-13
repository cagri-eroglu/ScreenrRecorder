import cv2
import numpy as np
from PIL import ImageGrab


codec = cv2.VideoWriter_fourcc (*"X264")
output = cv2.VideoWriter("output.mp4",codec,20.0,(1920,1080))

while True :       
    img_np = np.array(ImageGrab.grab())
    cv2.imshow("screen",img_np)
    output.write(img_np)
    

    if(cv2.waitKey(1)==15):
        break

output.release()    
cv2.destroyAllWindows()
