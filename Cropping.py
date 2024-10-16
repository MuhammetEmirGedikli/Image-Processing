import cv2
import numpy as np

resim=cv2.imread("directory/image.jpg")


kesit=resim[50:150,300:400]

kesit[:,:,0]=255

resim[0:100,0:100]=kesit

resim[400:450,300:350,]=(0,150,255)


#cv2.imshow("kesit alanı",kesit)
cv2.imshow("bayram resmi",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()