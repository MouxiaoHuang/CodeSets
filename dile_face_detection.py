# -*- coding: utf-8 -*-
# https://github.com/windandscreen/face_detection
import cv2
import dlib
import datetime


def detection(img):
    detector = dlib.get_frontal_face_detector()  # 使用默认的人类识别器模型
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dets = detector(gray, 1)
    for face in dets:
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.imshow("image", img)


def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        img = cv2.resize(img, (480, 320), interpolation = cv2.INTER_CUBIC)
        detection(img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    tic = datetime.datetime.now()
    main()
    toc = datetime.datetime.now()
    print(toc - tic)
