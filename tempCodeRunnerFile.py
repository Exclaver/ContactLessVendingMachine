import cv2
import speechrecognition as sp
import os

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




def Voicerec():
        cam = cv2.VideoCapture(0)
        counter=0
        #time.sleep(3)

        # If image will detected without any error, 
        # show result
        UserPath="user_img"
        while True:
            
            ret,frame=cam.read()
            # showing result, it take frame name and image 
            # output
            
            cv2.putText(frame,"stand straight for pic",(200,450),cv2.FONT_HERSHEY_COMPLEX_SMALL ,1,(0,0,255),2)

            cv2.imshow("frame",frame)
            key=cv2.waitKey(1)
            if key==27:
                cam.release()
                cv2.destroyAllWindows() 
                break
            counter+=1
            print(counter)
            if counter==100:
                try:
                    file_name=sp.speech()
        
                    
                    resize_img = cv2.resize(frame,(225,245),interpolation = cv2.INTER_AREA)
                    cv2.imshow("resized img",resize_img)
                    cv2.imwrite(os.path.join(UserPath,f"{file_name}.png"), resize_img)
                    ref=db.reference('Students').update({
                    file_name:
                            {
                                "name":file_name,
                                "Credits":69
                            }

        })
                    
                    counter=0           
                except:
                    break
                


  
