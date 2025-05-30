import cv2
import numpy as np

bgr = np.zeros((300, 300, 3), dtype=np.uint8)  
bgr[:,:,:] =[25, 44, 255]

img = cv2.imread('OpenCv_Python/img/img_zero.jpg')
C1 = img[:, :, 0]
C2 = img[:, :, 1]
C3 = img[:, :, 2] 

# Read the image in color
cv2.imshow("BGR", bgr)  
cv2.imshow("C1-C2-C3", np.hstack((C1, C2, C3)))   

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
cv2.imshow("RGB", img_rgb)  # Show the RGB image
cv2.waitKey(0)
cv2.destroyAllWindows()