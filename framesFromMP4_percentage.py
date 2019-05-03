import os
import sys
import cv2

vidn = 'scarif'
vidName = vidn + ".mp4"
absolueVidPath = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\avg-color-bar\\video\\" + vidName

try:
    vid = cv2.VideoCapture(absolueVidPath)

except OSError:
    print('Error: Unable to open/find the file specified')
except:
    print('Error: Make sure the file is in the video directory.')

try:
    fps = vid.get(cv2.CAP_PROP_FPS)
    totalFrameCount = int(vid.get(cv2.CAP_PROP_FRAME_COUNT)) 
    vidduration = totalFrameCount/fps 
    print('FPS: ' + str(fps))
    print('Frame Count: ' + str(totalFrameCount))
    print('Duration: ' + str(vidduration))

except ZeroDivisionError:
    print('Yeah dividing by zero is bad. The universe does not like that.')
    

modul = 50
percentToConvert = (modul/100)

maxFrames = int(totalFrameCount * percentToConvert)
print('Maximum Frames: ' + str(maxFrames))

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