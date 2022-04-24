import cv2 
import datetime
import os

  
# Load the cascade  
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')  
  
# To capture video from webcam.   
cap = cv2.VideoCapture(0)  
  
while True:  
    # Read the frame  
    _, img = cap.read()  
  
    # Convert to grayscale  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
    # Detect the faces  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) 
    count_faces=len(faces)
    temp_faces=0;
     
  
    # Draw the rectangle around each face  
    for (x, y, w, h) in faces:  
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
  
    print(count_faces)
    if count_faces==0:
        pass
    elif count_faces!=temp_faces:
        count_faces=temp_faces;
        e=datetime.datetime.now()
        name=f'{e.day}-{e.hour}-{e.minute}-{e.second}.jpg'
        cv2.imwrite(os.path.join('./captured_images', name),img)
    # Display  
    cv2.imshow('Video', img)  
  
    # Stop if escape key is pressed  
    k = cv2.waitKey(30) & 0xff  
    if k==27:  
        break  
          
# Release the VideoCapture object  
cap.release()  