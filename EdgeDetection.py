import cv2
import numpy as np

image=cv2.imread("direction/image.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)

"""
canny=cv2.Canny(blur,0,10)#kenar algılama için canny kullanılır hangi cismin köşelerini alacağımız parametreyi gireceğiz
#2. olarak eşik değerleri gireceğiz

"""

def autoCanny(blur,sigma=0.33):
    median=np.median(blur) #görüntüdeki piksel yoğunluklarının medyanını hesaplar
    lower=int(max(0,(1.0-sigma)*median))
    upper=int(min(255,(1.0-sigma)*median))
    canny=cv2.Canny(blur,lower,upper)#normalde örneğin 50 150 yazacakken yukarda girdiğimiz değerler otomatik geliyor

    return canny


wide=cv2.Canny(blur,10,220)
tight=cv2.Canny(blur,200,230)
auto= autoCanny(blur)


cv2.imshow("blurred image",blur)
cv2.imshow("edges",np.hstack([wide,tight,auto]))#tüm resimleri yan yana koyarak tek resim gibi gösterir









#cv2.imshow("blurred image",blur)
#cv2.imshow("canny image",canny)



cv2.waitKey(0)
cv2.destroyAllWindows()