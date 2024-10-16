import cv2
import numpy as np

#sol alt (x,y) ile sağ üst (x,y) koordinatlarını verince 2 nokta arasındaki alanı hesaplayıp oraya çerçeve içine alır

resim=cv2.imread("directory/image.jpg")

#resim[:,:,0]=255 #y x renk

cv2.rectangle(resim,(248,120),(330,208),[0,0,255],3) #oval parantez ile koordinat verdik x ve y bu sefer 4.değişken çerçeve kalınlığı




cv2.imshow("hababam sinifi",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()