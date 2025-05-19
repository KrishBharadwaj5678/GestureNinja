import cv2
from cvzone.HandTrackingModule import HandDetector
import mouse
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)
cam_w, cam_h = 640, 480
cap.set(3,cam_w)
cap.set(4,cam_h)
detector = HandDetector(detectionCon=0.65, maxHands=1)

# Total Screen Width and Height
scr_w, scr_h = 1919, 1079
frameR = 100 # It is a margin value to avoid edge glitches.

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    hands, img = detector.findHands(img) # Draw hand landmarks

    # Draw a rectangle, here (frameR,frameR) is the top-left corner and (cam_w - frameR , cam_h - frameR) is bottom-right corner
    cv2.rectangle(img,(frameR,frameR),(cam_w - frameR , cam_h - frameR),(255,0,255),2)

    if hands:
        lmList = hands[0]['lmList'] # Getting all hand landmarks
        ind_x, ind_y = lmList[8][0], lmList[8][1] # Taking Index finger x and y position
        cv2.circle(img,(ind_x,ind_y),5,(0,255,255),2)

        # np.interp() maps the fingertip coordinates from the camera frame (cam_w, cam_h) to screen coordinates (scr_w, scr_h).
        conv_x = int(np.interp(ind_x,(frameR, cam_w - frameR),(0,scr_w)))
        conv_y = int(np.interp(ind_y,(frameR, cam_h - frameR),(0,scr_h)))

        mouse.move(conv_x,conv_y) # Moves the mouse cursor to the mapped fingertip position on the screen.
        fingers = detector.fingersUp(hands[0])

        if fingers[4] == 1:
            # If the pinky finger is up (fingers[4] == 1), it simulates a mouse click hold.
            pyautogui.mouseDown()


    cv2.imshow("Camera Feed",img)
    cv2.waitKey(1)