import os

inputPath = "C:\\Users\\jeffrey.moody\\Documents\\GitHub\\avg-color-bar\\input"

for filename in os.listdir(inputPath):
    if filename.startswith("frame"):
        os.rename(filename, filename [0:])