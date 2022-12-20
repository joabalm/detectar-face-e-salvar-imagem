import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()

save_dir = 'fotos/'

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    i = 0
    faces_count = {}
    for face in faces:

        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y
        cv2.rectangle(frame, (x, y), (w + x, h + y), (0, 255, 0), 1)
        i = i + 1
        cv2.putText(frame, 'face' + str(i), (x - 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        face_img = frame[y:y + h, x:x + w]

        cv2.imwrite(save_dir + 'face' + str() + '.jpg', face_img)
        print('frame', frame)


    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 