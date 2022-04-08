import os
import time

import cv2
from moviepy.video.io.VideoFileClip import *

print('Welcome to the mp42image converter.')

file_path = input("File Path: ")
while not file_path.__contains__(".mp4"):
    print('Error no .mp4 file detected. Please try again.')
    file_path = input("File Path: ")
cam = cv2.VideoCapture(file_path)

output = input("Output directory: ")
while not os.path.exists(output):
    print('Error no output directory does not exist. Please try again.')
    output = input("Output directory: ")

if not os.path.exists(output + '\OutputFrames'):
    os.mkdir(output + '\OutputFrames')
output = output + '\OutputFrames'

change_fps = input('Change FPS (y/n): ')
while not (change_fps == 'y' or change_fps == 'n'):
    print('Invalid answer. Please try again.')
    change_fps = input('Change FPS (y/n): ')

if change_fps == 'y':
    fps = input('FPS: ')
    clip = VideoFileClip(file_path)
    clip.write_videofile(output + '\\video.mp4', fps=int(fps))
    file_path = output + '\\video.mp4'
    cam = cv2.VideoCapture(file_path)
    print('Successful changed FPS.')

frame_extension = input('Frame extensions (.png/.jpg): ')
while not (frame_extension == '.png' or frame_extension == '.jpg'):
    print('unknown file extension. Please try again.')
    frame_extension = input('Frame extensions (.png/.jpg): ')

# frame
currentframe = 0
output = output + '\Frame'

while True:

    ret, frame = cam.read()

    if ret:
        name = output + str(currentframe) + frame_extension
        print('Creating...' + name)

        cv2.imwrite(name, frame)

        currentframe += 1
    else:
        break

currentframe -= 1
print('Successful extracted ' + str(currentframe) + ' frames.')

cam.release()
cv2.destroyAllWindows()

time.sleep(3)
