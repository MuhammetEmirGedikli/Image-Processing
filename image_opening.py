import cv2
import numpy as np
"""
resim=cv2.imread("download.jpg",0) #bir resim importlamak için bunu kullanırız resimi cv2 aracılığı ile okuduğumuzu belirtiyoruz

#imread in yanına 0 koyarsak siyah beyaz yap demektir
#göstermek için de imshow fonksiyonu kullanılır

cv2.imshow("Ozengineer Logo",resim)


#cv2.imwrite("yeniresim.png",resim) # resim in renksiz halini de kaydetmek istiyorsak bu fonksiyonu kullanırız

cv2.waitKey(0) #bu temel iskelet açılan pencerenin kalmasını beklemeyi sağlar bir tuşa basana kadar pencereyi kapattırmaz

cv2.destroyAllWindows() # X butonuna bastığında tüm her şeyi kapat anlamına gelir

"""



resim=cv2.imread("directory/image.jpg")

cv2.imshow("Logo",resim)

# print(resim)  resmin pixelinin hangi değerlerden matrislerden oluştuğunu gösterir

print(resim.size) #resmin boyutunu(kapladığı alan değil) öğrenmemizi sağlar

print(resim.dtype) # it shows what data type it has

print(resim.shape) #sırasıyla genişlik yükseklik ve kaç kanaldan(renkten) oluşur onu söylüyor

resim=cv2.imread("directory/image.jpg",0)

#gri renge çevirmek onun üzerinden iş yapmak sistemin kanal sayısını 1 e düşüreceği için hızını arttırır ve daha kolay görüntü işler

print(resim.shape)

cv2.waitKey(0)

cv2.destroyAllWindows()



