#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Harshith Reddy | harshith.hr11@gmail.com

"""

import cv2
import face_recognition

# '0' parameter is the cam ID
video = cv2.VideoCapture(0)

#create variable for face locations
face_locations = []

while True:
    ret , frame = video.read()
    
    
    #convert BGR frame to RGB frame(face_recognition library uses it.)
    rgb_frame = frame[: , : , ::-1]
    #Identify face locations in frame.
    face_locations = face_recognition.face_locations(rgb_frame)
    #print(face_locations)
    
    #Draw a rectangle around face indentified.
    for top,right,bottom,left in face_locations:
        cv2.rectangle(frame,(left,top),(right,bottom),(0,255,0),2)
    
    cv2.imshow('face_detection_code',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
