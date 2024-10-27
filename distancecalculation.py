import cv2
import numpy as np

# Kameranın iç parametreleri
focal_length = 1000  # Örnek değer, gerçek fokal uzaklığını kullanmalısınız

# Objeyi ölçtüğümüz gerçek dünyadaki boyutları
real_object_height = 3.5  # Örnek değer, gerçek boyutları kullanmalısınız

# Fotoğrafı yükle
image = cv2.imread("directory/distance_to_camera_2ft.jpg")

# Fotoğraf üzerinde objenin boyutlarını ölç
object_width_pixels = 248   # Örnek değer, objenin piksel cinsinden genişliğini ölçmelisiniz
object_height_pixels = 543.45  # Örnek değer, objenin piksel cinsinden yüksekliğini ölçmelisiniz

# Objeyi algıla ve çerçeveleme (örnek olarak yüz algılama kullanılıyor)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

if len(faces) > 0:
    (x, y, w, h) = faces[0]
    object_height_pixels = h

# Uzaklığı hesapla
distance = (focal_length * real_object_height) / object_height_pixels

# Uzaklığı yazdır
print("Uzaklık:", distance, "metre")

# Sonucu görselleştir (isteğe bağlı)
cv2.putText(image, f"Uzaklık: {distance:.2f} santimetre", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
