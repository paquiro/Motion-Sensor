"""My Raspberry pi2B record a mean of 360 frames each 26-28 seconds with
Eye Toy camera of PlayStation 3."""

import numpy as np
import cv2
import time
import subprocess

#return a positive number if success.
#return -1 if failure
def selectFrameRate ():
    cap = cv2.VideoCapture(0);
    if(not cap.isOpened()):
        return -1
    # Number of frames to capture
    num_frames = 120;

    # Start time
    start = time.time()

    # Grab a few frames
    for i in xrange(0, num_frames) :
        ret, frame = cap.read()

    # End time
    end = time.time()

    # Time elapsed
    seconds = end - start

    # Release cap
    cap.release()

    return num_frames/seconds

#return a name in format media/video/DD-MM-AAAA_HH:MM:SS.avi if success
#return a string with the text 'error'
def video (seconds, frameRate):
    cap = cv2.VideoCapture(0)
    if(not cap.isOpened()):
        return "error"

    # Define the codec and create VideoWriter object
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    name = "media/video/" + time.strftime("%d-%m-%Y_%X")+".avi"
    out = cv2.VideoWriter(name, fourcc, frameRate, (640,480))
    program_starts = time.time()
    result = subprocess.Popen(["ffprobe", name], stdout = subprocess.PIPE, stderr = subprocess.STDOUT, shell=True)
    nFrames=0
    while(nFrames<seconds*frameRate):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            nFrames += 1
        else:
            break
    cap.release()
    return name
