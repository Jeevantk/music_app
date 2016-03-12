from cv2 import *
for i in range(0,42):
    img=imread(str(i)+".jpg",0)
    changed=resize(img,(400,40))
    th3 = adaptiveThreshold(changed,255,ADAPTIVE_THRESH_GAUSSIAN_C,THRESH_BINARY,11,2)
    imwrite(str(i)+".jpg",th3)
    
