import numpy as np
import pandas as pd
import cv2
import time
import os
import csv
from datetime import datetime
from PIL import Image

def takeImages():
    Id = int(input('enter ID: '))
    Name = input('enter NAME: ')
    
    vidcap = cv2.VideoCapture(-1)
    detectorcas = cv2.CascadeClassifier('/home/adarsh1927/Downloads/haarcascade_frontalface_default.xml')
    samplenum = 0
    while(True):
        ret, img = vidcap.read()        
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detectorcas.detectMultiScale(grayimg, 1.3, 5)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),1)
            samplenum += 1
            cv2.imwrite('/home/adarsh1927/trainingImage/'+Name+"."+str(Id)+"."+str(samplenum)+".jpg", grayimg[y:y+h,x:x+w])
            cv2.imshow('frame',img)
        if cv2.waitKey(100) & 0XFF == ord('q'):
            break
        elif samplenum>60:
                break
    vidcap.release()
    cv2.destroyAllWindows()
    row = [Id, Name]
    with open('/home/adarsh1927/StudentDetails/StudentDetail.csv','a+') as csvFile :
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    print("image saved for ID:",Id,'and Name:',Name)
    
def trainImage():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    detector = cv2.CascadeClassifier('/home/adarsh1927/haarcascade_frontalface_default.xml')
    faces,Id = getImagesAndLabels('/home/adarsh1927/trainingImage')
    recognizer.train(faces, np.array(Id))
    recognizer.save('/home/adarsh1927/trainingImageLabel/Trainner.yml')
    print('Image Trained')
    
def getImagesAndLabels(path) :
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    print(path,'\n',imagePaths)
    faces = []
    Ids = []
    for imagePath in imagePaths:
        pilimage =Image.open(imagePath).convert('L')
        imageNp = np.array(pilimage,'uint8')
        Id = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(imageNp)
        Ids.append(Id)
    return faces, Ids

def trackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('/home/adarsh1927/trainingImageLabel/Trainner.yml')
    detector = cv2.CascadeClassifier('/home/adarsh1927/haarcascade_frontalface_default.xml')
    vidcap = cv2.VideoCapture(-1)
    df = pd.read_csv("/home/adarsh1927/StudentDetails/StudentDetail.csv", names=['Id','Name'])
    font = cfont= cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'name', 'Date','Time']
    attendance = pd.DataFrame(columns =col_names)
    while True:
        ret, img = vidcap.read()
        grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(grayimg, 1.2, 5)    
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h),(225,0,0), 1)
            Id, differ = recognizer.predict(grayimg[y:y+h, x:x+w])

            if (differ < 50) :
                now = datetime.now()
                date = now.strftime('%d/%m/%Y')
                timeStamp = now.strftime('%H:%M:%S')
                print(timeStamp)
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id)+'-'+aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]
            else:
                Id = 'Unknown'
                tt = str(Id)
            if differ > 75 :
                noOfFile = len(os.listdir('Images_Unknown'))+1
                cv2.imwrite('/home/adarsh1927/ImageUnknown/Image'+str(noOfFile)+
                                '.jpg',img[y:y+h, x:x+w])
            cv2.putText(img, str(tt),(x, y+h), font, 1, (255, 255, 255),2)
        attendance = attendance.drop_duplicates(subset = ['Id'], keep = 'first')
        cv2.imshow('Recognition',img)
        if cv2.waitKey(100) == ord('q'):
            break
    now = datetime.now()
    date = now.strftime('%d/%m/%y')
    timetStamp = now.strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(':')
    attendance.to_csv('/home/adarsh1927/attendance/aten.csv', index = False)
    vidcap.release()
    cv2.destroyAllWindows()
    print (attendance)

    
                    
                    
takeImages()
trainImage()
trackImages()
            
            
            
            
            
        
        
        
    
