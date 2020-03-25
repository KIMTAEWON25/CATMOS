from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys


#Create the haar cascadefaceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalcatface.xml")

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
#camera.resolution 
camera.resolution = (480, 384)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(480, 384))
# allow the camera to warmup
time.sleep(0.1)
lastTime = time.time()*1000.0
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    #image = frame.array
    image = cv2.imread('cats.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=1,
    minSize=(30, 30),
#    flags = cv2.CV_HAAR_SCALE_IMAGE
    flags = cv2.CASCADE_SCALE_IMAGE
    )
    print (time.time()*1000.0-lastTime," Found {0} faces!".format(len(faces)) )
    
    lastTime = time.time()*1000.0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y),(x+w, y+h), (255, 0, 0), 1) 
        #cv2.circle(image, (int(x+w/2), int(y+h/2)), int((w+h)/3), (255, 255, 255), 3)
        
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)    
	# if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
        
  
        

