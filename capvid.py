import cv2
import os


current_directory = os.getcwd()
subject_name = input("Enter your name: ")
subject_directory = os.path.join(current_directory, subject_name)
if not os.path.exists(subject_directory):
   os.makedirs(subject_directory)

print(subject_directory)

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = subject_name+ str(img_counter)+".jpg".format(img_counter)
        cv2.imwrite(subject_directory+'/'+img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
