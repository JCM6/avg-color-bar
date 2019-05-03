import os
import sys
import cv2


absolueVidPath = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\avg-color-bar\\video\\sarif.mp4"
vid = cv2.VideoCapture(absolueVidPath)

try:
        #creation of the destination directory
        if not os.path.exists('data'):
            os.makedirs('data')
except OSError:
    print('Error: Creating directory of data.')

currentframe = 0

while(True):

    #read current frame
    ret, frame = vid.read()

    if ret:
            #checks to see if there are more frames to go.
            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)

            #write extracted images
            cv2.imwrite(name, frame)
            currentframe += 1
    else:
        break

vid.release()
cv2.destroyAllWindows()