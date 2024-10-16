import time
import mediapipe as mp
import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

mpHand=mp.solutions.hands
hands=mpHand.Hands()

mpDraw=mp.solutions.drawing_utils

tipIds=[4,8,12,16,20]



while True:

    landmarklist=[]

    success,img= cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)

    print(results.multi_hand_landmarks)

    lmlist = []

    if(results.multi_hand_landmarks):
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS)
            for id,lm in enumerate(handLms.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)

                lmlist.append([id,cx,cy])


    if(len(lmlist)!=0):
        fingers=[]


        if lmlist[tipIds[0]][1] < lmlist[tipIds[1]][1]:

            cv2.putText(img,("left hand"),(80,125),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),8)

            if lmlist[tipIds[0]][1] < lmlist[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)

        elif lmlist[tipIds[0]][1] > lmlist[tipIds[1]][1]:

            cv2.putText(img , ("right hand") , (80 , 125) , cv2.FONT_HERSHEY_PLAIN , 3 , (255 , 0 , 0) , 8)
            if lmlist[tipIds[0]][1] < lmlist[tipIds[0]-1][1]:
                fingers.append(0)
            else:
                fingers.append(1)


        for nokta in range(1,5):
            if lmlist[tipIds[nokta]][2] < lmlist[tipIds[nokta] - 1][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalF=fingers.count(1)

        cv2.putText(img , str(totalF) , (30 , 30) , cv2.FONT_HERSHEY_PLAIN , 3 , (255 , 0 , 0) , 2)


    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    cv2.imshow("img",img)
    


 