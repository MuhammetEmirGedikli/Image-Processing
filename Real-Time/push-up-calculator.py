import cv2
import numpy as np
import mediapipe as mp
import math
import time

def findAngle(img,p1,p2,p3,lmlist,draw=True):
    x1, y1=lmlist[p1][1:]
    x2, y2=lmlist[p2][1:]
    x3, y3=lmlist[p3][1:]

    #açı hesapla
    angle= math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
    if angle < 0:
        angle+=360

    if draw:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),3)
        cv2.line(img,(x3,y3),(x2,y2),(0,0,255),3)

        cv2.circle(img , (x1 , y1) , 10 , (0 , 255 , 255) , cv2.FILLED)
        cv2.circle(img , (x2 , y2) , 10 , (0 , 255 , 255) , cv2.FILLED)
        cv2.circle(img , (x3 , y3) , 10 , (0 , 255 , 255) , cv2.FILLED)

        cv2.circle(img , (x1 , y1) , 15 , (0 , 255 , 255) , cv2.FILLED)
        cv2.circle(img , (x2 , y2) , 15 , (0 , 255 , 255) , cv2.FILLED)
        cv2.circle(img , (x3 , y3) , 15 , (0 , 255 , 255) , cv2.FILLED)

        cv2.putText(img,str(int(angle)),(x2+100,y2+40),cv2.FONT_HERSHEY_PLAIN,6,(0,255,255))
        return angle
        





cap=cv2.VideoCapture(0)

mpPose=mp.solutions.pose
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils

dir=0
count=0
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results=pose.process(imgRGB)
    lmlist=[]
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS) #çizimleri yaptırmak için kullanıyoruz

        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,_=img.shape
            cx,cy=int(lm.x*w), int(lm.y*h)
            lmlist.append([id,cx,cy])
        #print(lmlist)

        if len(lmlist) !=0:

            #push-up
            angle=findAngle(img,11,13,15,lmlist) #açı hesaplamak için yukarıdaki fonksiyona gönderiyoruz
            per=np.interp(angle,(190,300),(0,100))
            print(angle)
            if per==100:
                if dir==0:
                    count+=0.5
                    dir=1
            if per==0:
                if dir==1:
                    count+=0.5
                    dir=0

            print(count)
            

            cv2.putText(img,str(int(count)),(45,125),cv2.FONT_HERSHEY_PLAIN,10,(255,0,0),10)



    if cv2.waitKey(1) and 0xFF==ord('q'):    
        break
    
    cv2.imshow("video=",img)
    