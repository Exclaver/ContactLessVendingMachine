import cv2
from simple_facerec import SimpleFacerec
import time
import os
import OpenCVModule as htm
# import controller as cnt

sfr=SimpleFacerec()
sfr.load_encoding_images("images/")

wCam,hCam=640,480

cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0

detector=htm.handDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]

name1=0
name=0




while True:
    ret,frame=cap.read()
    face_location,face_names=sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_location,face_names):              
        print(name)
        name1=name

                # for face_loc,name in zip(face_location,face_names):
                    # y1,x1,y2,x2=face_loc[0],face_loc[1],face_loc[2],face_loc[3]
                    # cv2.putText(frame,name,(x1,y1-10),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),2)

                    # cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,200),4)
                    
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(frame,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        cap.release()
        cv2.destroyAllWindows()               
    while name=="":
         print("no Face detected")
    while name=="Unknown":
         print("Unknown face")
    while name=="Devansh":
            
            success,frame=cap.read()
            frame=detector.findHands(frame)
            lmList=detector.findPosition(frame,draw=False)
                        # print(lmList)
                        
            if len(lmList)!=0:
                fingers=[]

                #thumb
                if lmList[tipIds[0]][1]>lmList[tipIds[0]-1][1]:
                        fingers.append(1)
                else:
                        fingers.append(0)


                #fingers
                for id in range(1,5):

                    if lmList[tipIds[id]][2]<lmList[tipIds[id]-2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                # print(fingers)
                totalFingers=fingers.count(1)
                print(totalFingers) 
                # cnt.led(totalFingers)     
            cTime=time.time()
            fps=1/(cTime-pTime)
            pTime=cTime
            cv2.putText(frame,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
            cv2.imshow("Frame",frame)
            key=cv2.waitKey(1)
            if key==27:
                cap.release()
                cv2.destroyAllWindows()  

                
            
        

            
        


            
    






    
