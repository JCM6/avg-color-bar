import os

absinputPath = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\avg-color-bar\\images"
inputPath = "data\\"
outputPath = "images\\"

itr = 0

for filename in os.listdir(inputPath):
        destination = outputPath + str(itr) + '.png'
        source = inputPath + filename
        os.rename(source, destination)
        itr += 1