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

frame_extension = input('Frame extensions (.png/.jpg): ')
while not (frame_extension == '.png' or frame_extension == '.jpg'):
    print('unknown file extension. Please try again.')
    frame_extension = input('Frame extensions (.png/.jpg): ')

few_images_in_one_directory = input('Every 79 images in one directory (y/n): ')
while not (few_images_in_one_directory == 'y' or few_images_in_one_directory == 'n'):
    print('Invalid answer. Please try again.')
    few_images_in_one_directory = input('Every 79 images in one directory (y/n): ')

if few_images_in_one_directory == 'y':
    if not os.path.exists(output + '\Folder 1'):
        os.mkdir(output + '\Folder 1')
    output_old = output + '\Folder 1'
else:
    output_old = output

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

# frame
currentframe = 0
current_name_frame = 0
output_for_images = output_old + '\Frame'
folder_number = 1

while True:

    ret, frame = cam.read()

    if ret:
        name = output_for_images + str(currentframe) + frame_extension
        name_new = output_for_images + str(current_name_frame) + frame_extension
        print('Creating...' + name_new)

        cv2.imwrite(name, frame)

        os.rename(name, name_new)
        currentframe += 1
        current_name_frame += 1
    else:
        break
    if few_images_in_one_directory == 'y' and current_name_frame == 80:
        folder_number += 1
        os.mkdir(output + '\Folder ' + str(folder_number))
        current_name_frame = 0
        output_for_images = output + '\Folder ' + str(folder_number) + '\Frame'

currentframe -= 1
print('Successful extracted ' + str(currentframe) + ' frames.')

cam.release()
cv2.destroyAllWindows()

time.sleep(3)
