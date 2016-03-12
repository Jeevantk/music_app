from cv2 import *
for i in range(6,54):
    img=imread(str(i)+".jpg",0)
    changed=resize(img,(400,40))
    th3 = adaptiveThreshold(changed,255,ADAPTIVE_THRESH_GAUSSIAN_C,THRESH_BINARY,11,2)
    imwrite(str(i+48)+".jpg",th3)
    
