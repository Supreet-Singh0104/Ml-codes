# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2

#Create cameraobject
cam = cv2.VideoCapture(0)

while True:
    success,img=cam.read()
    if not success:
        print("Reading Camera Failed!")
        
    cv2.imshow("Image Window",img)
    cv2.waitKey(1) # PAuse here for 1 ms before you read the next image

