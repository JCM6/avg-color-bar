import os

absinputPath = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\avg-color-bar\\images"
inputPath = "images\\"
outputPath = "output\\"
fileBase = "frame_00_delay-0.1s.gif"

itr = 0

print(str(os.listdir(inputPath)))

for filename in os.listdir(inputPath):
        destination = inputPath + str(itr) + '.png'
        source = inputPath + filename
        os.rename(source, destination)
        itr += 1