import os
import sys
import cv2

vidn = 'scarif'
vidName = vidn + ".mp4"
absolueVidPath = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\avg-color-bar\\video\\" + vidName
vid = cv2.VideoCapture(absolueVidPath)
maxFrames = 200

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

    if ret and currentframe < (maxFrames + 1):
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