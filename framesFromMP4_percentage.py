import os
import sys
import cv2
import frameRenamer as fr

vidn = 'scarif'
vidName = vidn + ".mp4"
absolueVidPath = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\avg-color-bar\\video\\" + vidName

try:
    vid = cv2.VideoCapture(absolueVidPath)

except OSError:
    print('Error: Unable to open/find the file specified.')

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
    

modul = 1
percentToConvert = (modul/100)

maxFrames = int(totalFrameCount * percentToConvert)
print('Maximum Frames: ' + str(maxFrames))
print('Starting video file processing.......')
try:
        #creation of the destination directory
        if not os.path.exists('data'):
            os.makedirs('data')
        print('Creating data directory for first run')

except OSError:
    print('Error: Creating directory of data.')
    print('Error caused by an issue creating the data folder for the first time.')

#Start Frame
currentframe = 0

while(True):

    #Read current frame
    ret, frame = vid.read()

    #Iterate through frames until max frame count is reached.
    if ret and currentframe < (maxFrames + 1):

            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)

            #Write extracted frames
            cv2.imwrite(name, frame)
            currentframe += 1
    else:
        print('Extracting frames is complete.')
        break

try:
    vid.release()
    cv2.destroyAllWindows()
    print('cv2 Window Successfully Cleared')

except:
    print('Something went wrong releasing the video.')

print('Starting file renaming now........')
dataPath = 'data\\'
outputPath = "images\\"
itr = 0

for filename in os.listdir(dataPath):
    destination = outputPath + str(itr) + '.png'
    source = dataPath + filename
    os.rename(source, destination)
    itr += 1

print('File renaming complete!')
print('Staring histogram processing......')



