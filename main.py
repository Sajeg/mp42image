import os
import cv2

print('Welcome to the mp42image converter.')

file_path = input("File Path: ")
while not file_path.__contains__(".mp4"):
    print('Error no .mp4 file detected. Please try again.')
    file_path = input("File Path: ")
cam = cv2.VideoCapture(file_path)

change_fps = input('Change FPS (y/n): ')
while not (change_fps == 'y' or change_fps == 'n'):
    print('Invalid answer. Please try again.')
    change_fps = input('Change FPS (y/n): ')

if change_fps == 'y':
    fps = input('FPS: ')
    cam.set(cv2.CAP_PROP_FPS, int(fps))
    print('Successful changed FPS.')

output = input("Output directory: ")
if not os.path.exists(output + '\OutputFrames\ '):
    os.mkdir(output + '\OutputFrames\ ')
new_output = output + '\OutputFrames\Frame'

frame_extension = input('Frame extensions (.png/.jpg): ')
while not (frame_extension == '.png' or frame_extension == '.jpg'):
    print('unknown file extension. Please try again.')
    frame_extension = input('Frame extensions (.png/.jpg): ')

# frame
currentframe = 0

while True:

    ret, frame = cam.read()

    if ret:
        name = new_output + str(currentframe) + frame_extension
        print('Creating...' + name)

        cv2.imwrite(name, frame)

        currentframe += 1
    else:
        break

print('Successful extracted ' + currentframe + ' frames.')

cam.release()
cv2.destroyAllWindows()
