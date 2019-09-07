#Import section
import cv2

#Defineclassifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')# trained classifier

#Read the image 
img = cv2.imread('Untitled.jpg')

#covert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect face on gray image
faces = face_cascade.detectMultiScale(img_gray,1.1,4)#(image, scaleFactor, minNeighbors)

#Iterate over faces
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)

#Display the output
cv2.imshow('Image',img)
cv2.waitKey()
