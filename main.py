import os
import cv2

print('Welcome to the mp42jpg converter.')

file_path = input("File Path: ")
while not file_path.__contains__(".mp4"):
    print('Error no .mp4 file detected. Please try again.')
    file_path = input("File Path: ")
cam = cv2.VideoCapture(file_path)

if input('Change FPS (y/n): ') == 'y':
    fps = input('FPS: ')
    cam.set(cv2.CAP_PROP_FPS, int(fps))
    print('Successful changed FPS.')

output = input("Output directory: ")
if not os.path.exists(output + '\OutputFrames\Frame'):
    os.mkdir(output + '\OutputFrames\ ')
new_output = output + '\OutputFrames\Frame'

# frame
currentframe = 0

while True:

    ret, frame = cam.read()

    if ret:
        name = new_output + str(currentframe) + '.png'
        print('Creating...' + name)

        cv2.imwrite(name, frame)

        currentframe += 1
    else:
        break

print('Successful extracted all frames.')

cam.release()
cv2.destroyAllWindows()