import cv2
import numpy as np

resim1=cv2.imread("directory/image.jpg")
resim2=cv2.imread("directory/image.jpg")

cv2.imshow("ozanguven",resim1)
cv2.imshow("cemyilmaz",resim2)

toplam=cv2.add(resim1,resim2)

agirliklitoplama=cv2.addWeighted(resim1,0.7,resim2,0.3,0)#saydamlığı ayarlıyoruz ilk fotodan %70 oranıunda bi opaklık 2.sinde %30,son parametre 0 her zaman

cv2.imshow("agirlikli toplama",agirliklitoplama)


cv2.imshow("toplanmis resimler",toplam)



cv2.waitKey(0)
cv2.destroyAllWindows()