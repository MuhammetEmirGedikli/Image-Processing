import cv2
import numpy as np

resim=cv2.imread("directory/image.jpg")

ikikatbuyuk=cv2.pyrUp(resim)

ikikatkucuk=cv2.pyrDown(resim)

print("orijinal resim",resim.shape)
print("iki kat buyuk resim",ikikatbuyuk.shape)
print("iki kat kucuk resim",ikikatkucuk.shape)

cv2.imshow("natalie kucuk",ikikatkucuk)
cv2.imshow("natalie normal",resim)
cv2.imshow("natalie iki kat",ikikatbuyuk)

cv2.waitKey(0)
cv2.destroyAllWindows()