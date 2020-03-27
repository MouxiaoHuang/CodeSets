import cv2
import dlib
import math
import numpy as np
"""
face_detector = dlib.cnn_face_detection_model_v1('face_detector/mmod_human_face_detector.dat')

img = cv2.imread('images/1.jpg')
detected_faces = face_detector(img, 1)
print('检测到的人脸数为：', len(detected_faces))

for i in range(len(detected_faces)):
    face = detected_faces[i].rect
    left = face.left()
    top = face.top()
    right = face.right()
    bottom = face.bottom()
    cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)
cv2.imshow('image', img)
cv2.waitKey(0)
"""

face_detector = dlib.cnn_face_detection_model_v1('face_detector/mmod_human_face_detector.dat')
landmark_detector = dlib.shape_predictor('face_detector/shape_predictor_68_face_landmarks.dat')
img = cv2.imread('images/1.jpg')

### 旋转处理 ###
def rotate_bound(image,angle):#angle > 0为顺时针
    #获取图像的尺寸
    #旋转中心
    (h,w) = image.shape[:2]
    (cx,cy) = (w/2,h/2)
    
    #设置旋转矩阵
    M = cv2.getRotationMatrix2D((cx,cy),-angle,1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])
    
    # 计算图像旋转后的新边界
    nW = int((h*sin)+(w*cos))
    nH = int((h*cos)+(w*sin))
    
    # 调整旋转矩阵的移动距离（t_{x}, t_{y}）
    M[0,2] += (nW/2) - cx
    M[1,2] += (nH/2) - cy
    
    return cv2.warpAffine(image,M,(nW,nH))

def calAngle(p8col, p8row, p33col, p33row):
    tanAnlge = (p8col-p33col)*1.0/((p8row-p33row)*1.0)
    Angle = math.atan(tanAnlge) * 180 / 3.14
    return Angle

img = rotate_bound(img, calAngle(148,177,112,147))

detected_faces = face_detector(img, 1)
if(len(detected_faces)==0):
    print('No faces are detected!')
else:
    print('检测到人脸数：', len(detected_faces))
    for i in range(len(detected_faces)):
        face = detected_faces[0].rect
        left = face.left()
        top = face.top()
        right = face.right()
        bottom = face.bottom()
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

        lm = landmark_detector(img, face)
        for i in range(68):
            cv2.circle(img, (lm.part(i).x, lm.part(i).y),5,(0,255,0), -1, 8)
            cv2.putText(img,str(i),(lm.part(i).x,lm.part(i).y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,2555,255))
        print(lm.part(33))
        print(lm.part(8))
    cv2.imshow('image', img)
    cv2.waitKey(0)


"""
{
	IdxRange jaw;       // [0 , 16]
	IdxRange rightBrow; // [17, 21]
	IdxRange leftBrow;  // [22, 26]
	IdxRange nose;      // [27, 35]
	IdxRange rightEye;  // [36, 41]
	IdxRange leftEye;   // [42, 47]
	IdxRange mouth;     // [48, 59]
	IdxRange mouth2;    // [60, 67]
}

"""