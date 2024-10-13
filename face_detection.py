import cv2
import mediapipe as mp

cap=cv2.VideoCapture(0)
mpFaceDetection=mp.solutions.face_detection
faceDetection=mpFaceDetection.FaceDetection(0.20)
while True:
    success,img=cap.read()

    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=faceDetection.process(imgRGB)

    #print(results.detections) sonucu görmek için detections yazıyoruz
    

    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxC=detection.location_data.relative_bounding_box #aldığı suratımızın görüntüsünün görünmez bir kare içerisindeki koordinatları
            print(bboxC)q
            h,w,_=img.shape
            bbox=int(bboxC.xmin*w),int(bboxC.ymin*h),int(bboxC.width*w),int(bboxC.height*h)
            cv2.rectangle(img,bbox,(0,255,255),2)
        
            


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    cv2.imshow("img",img)
