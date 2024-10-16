import cv2

import numpy as np

resim=cv2.imread("directory/image.jpg")

resim[50,30]=[255,255,255] #pikseli değiştirdik pikselin rengini beyaz yaptık

for i in range(100):
    resim[50,i]=[255,255,255]

cv2.imshow("joker",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
