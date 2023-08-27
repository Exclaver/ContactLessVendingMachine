import cv2
from simple_facerec import SimpleFacerec
import time
import os
import OpenCVModule as htm
# import controller as cnt
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://contactlessvending-default-rtdb.firebaseio.com/",
    'storageBucket':"contactlessvending.appspot.com"
})


sfr=SimpleFacerec()
sfr.load_encoding_images("images/")

bucket=storage.bucket()
mainCounter=0
selectionSpeed=9
wCam,hCam=640,480
cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime=0
name=0
modePositions=[(1136,196),(1000,384),(1136,581),(1050,384)]
counter=0
counterPause=0
selectionList=[-1,-1,-1]
AuthenticationList=[-1]
ImgBackground=0
modeType=4
selections=-1
ImgStudent=[]




detector=htm.handDetector(detectionCon=0.75)
tipIds=[4,8,12,16,20]



#importing all moodes to list
folderPathModes="Resources/Modes"
listImgModesPath=os.listdir(folderPathModes)
listImgModes=[]
for imgModePath in listImgModesPath:
     listImgModes.append(cv2.imread(os.path.join(folderPathModes,imgModePath)))

#importing all the icons to list
folderPathIcons="Resources/Icons"
listImgIconsPath=os.listdir(folderPathIcons)
listImgIcons=[]
for imgIconsPath in listImgIconsPath:
     listImgIcons.append(cv2.imread(os.path.join(folderPathIcons,imgIconsPath)))



def Output():
    
    global pTime
    global ImgBackground
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(frame,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    if name=="Devansh":
     cv2.putText(frame,"Welcome Devansh",(200,450),cv2.FONT_HERSHEY_COMPLEX_SMALL ,1,(255,53,153),2)
    elif name=="Unknown":
     cv2.putText(frame,"Unknown Face",(200,450),cv2.FONT_HERSHEY_COMPLEX_SMALL ,1,(255,53,153),2)
    else:
        cv2.putText(frame,"No Face Detected",(200,450),cv2.FONT_HERSHEY_COMPLEX_SMALL ,1,(255,53,153),2)
   
    ImgBackground=cv2.imread("Resources\Background.jpg")
    ImgBackground[139:139+480,50:50+640]=frame
    ImgBackground[0:720,847:1280]=listImgModes[modeType]
    if mainCounter!=0 and name!="Unknown":
     cv2.putText(ImgBackground,str(studentInfo['Credits']),(980,500),cv2.FONT_HERSHEY_COMPLEX ,1,(255,0,0),2)
     ImgBackground[150:150+245,953:953+225]=ImgStudent
    if authloop==0 and selectionList[0]!=-1 and selectionList[1]!=-1 and selectionList[2]!=-1:
         cv2.putText(ImgBackground,str(studentInfo['Credits']),(980,500),cv2.FONT_HERSHEY_COMPLEX ,1,(255,0,0),2)
         print("oolah")

    if selections==4:
        cv2.ellipse(ImgBackground,(1050,445),(100,0),180,0,counter*4.6,(255,0,0),15)
    else:
        cv2.ellipse(ImgBackground,modePositions[selections-1],(103,103),0,0,counter*selectionSpeed,(0,153,0),15)
    #iconlist
    if selectionList[0]!=-1:
     ImgBackground[636:636+65,133:133+65]=listImgIcons[selectionList[0]-1]  
    if selectionList[1]!=-1:
     ImgBackground[636:636+65,340:340+65]=listImgIcons[2+selectionList[1]]
    if selectionList[2]!=-1:
     ImgBackground[636:636+65,542:542+65]=listImgIcons[5+selectionList[2]]

    cv2.imshow("Background",ImgBackground)
    key=cv2.waitKey(1)
    if key==27:
        cap.release()
        cv2.destroyAllWindows()  
    
#authentication

while AuthenticationList[0]!=4:
     authloop=1
     ret,frame=cap.read()
     face_location,face_names=sfr.detect_known_faces(frame)
     for face_loc,name in zip(face_location,face_names):              
        print(name)
        name1=name    
        if mainCounter==0:
                mainCounter=1
     if mainCounter!=0 and name!="Unknown":
         if mainCounter==1:
             #Data from Database
             studentInfo=db.reference(f'Students/{name}').get()
             print(studentInfo) 
             #Image from database
             blob=bucket.get_blob(f'images/{name}.jpg')
             array=np.frombuffer(blob.download_as_string(),np.uint8)
             ImgStudent=cv2.imdecode(array,cv2.COLOR_BGRA2BGR)
             #update credits
          #    if selectionList==[]
          #    ref=db.reference(f'Students/{name}')
          #    studentInfo['Credits']+=10  
          #    ref.child('Credits').set(studentInfo['Credits'])
     
     Output()
     if name=="Unknown":
         print("Unknown face")
     while name=="Devansh" and AuthenticationList[0]!=4:
            
            
            success,frame=cap.read()
            frame=detector.findHands(frame)
            lmList=detector.findPosition(frame,draw=False)
                        # print(lmList)             
            if len(lmList)!=0 and counterPause==0 and modeType<5:
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
                print(fingers) 

               #  if fingers==[0,1,0,0,0]:
               #       if selections!=1:
               #          counter=1
               #       selections=1
                if fingers==[0,1,1,1,1]:
                     if selections!=4:
                        counter=1
                     selections=4                                            
                else:
                     selections=-1
                     counter=0
                #print(selections)
                if counter>0:
                     counter+=1
                    #  print(counter)                     
                     if counter*selectionSpeed>360:
                          AuthenticationList[0]=selections                         
                          counter=0
                          selections=-1
                          counterPause=1
                         #  print(modeType)
            #pause function  
            if counterPause>0:
                 counterPause+=1
                 if counterPause>40:
                      counterPause=0
            print(AuthenticationList)
            
          
            Output()
     if name!="Devansh" and name!="Unknown":
          print("No Face Detected")
     
     
#maincode
mainCounter=0
counter=0
counterPause=0
ImgBackground=0
modeType=0
selections=-1
mainCounter=0
creditCounter=0
while True:
     authloop=0
     ret,frame=cap.read()
     face_location,face_names=sfr.detect_known_faces(frame)
     for face_loc,name in zip(face_location,face_names):              
        print(name)
        name1=name         
        
        

     Output()
     if name=="Unknown":
         print("Unknown face")

     while name=="Devansh":
            
            if selectionList==[2,3,2] and creditCounter<1:
               ref=db.reference(f'Students/{name}')
               studentInfo['Credits']-=10  
               ref.child('Credits').set(studentInfo['Credits'])
               creditCounter=1
            success,frame=cap.read()
            frame=detector.findHands(frame)
            lmList=detector.findPosition(frame,draw=False)
                        # print(lmList)       
            if len(lmList)!=0 and counterPause==0 and modeType<3:
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
                print(fingers) 

                if fingers==[0,1,0,0,0]:
                     if selections!=1:
                        counter=1
                     selections=1
                elif fingers==[0,1,1,0,0]:
                     if selections!=2:
                        counter=1
                     selections=2
                elif fingers==[0,1,1,1,0]:
                     if selections!=3:
                        counter=1
                     selections=3
                else:
                     selections=-1
                     counter=0
                if counter>0:
                     counter+=1
                    #  print(counter)
                     cv2.ellipse(ImgBackground,modePositions[selections-1],(103,103),0,0,counter*selectionSpeed,(0,156,0),15)

                     if counter*selectionSpeed>360:
                          selectionList[modeType]=selections
                          modeType+=1
                          counter=0
                          selections=-1
                          counterPause=1
                         #  print(modeType)
            #pause function  
            if counterPause>0:
                 counterPause+=1
                 if counterPause>40:
                      counterPause=0
            
            print(selectionList)
            Output()
     if name!="Devansh" and name!="Unknown":
          print("No Face Detected")