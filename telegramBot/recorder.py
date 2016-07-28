import numpy as np
import cv2
import time
import subprocess


def video (seconds):
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.cv.CV_FOURCC('M','P','E','G')
    name = "videos/"+time.strftime("%d-%m-%Y_%X")+".avi"
    out = cv2.VideoWriter(name, fourcc, 30.0, (640,480))

    program_starts = time.time()
    now = time.time()
    result = subprocess.Popen(["ffprobe", name], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    while(now-program_starts<seconds):
        now = time.time()
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
        else:
            break
