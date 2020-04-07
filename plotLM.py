import cv2
import numpy as np


def plotLM68(image, frame_index):
    pathLM = 'annot/' + str(frame_index).zfill(6) + '.pts'
    landmark = []
    with open(pathLM, 'r') as f:
        data = f.readlines() # 列表，68个landmark为4至71行
        for i in range(3, 71):
            temp = data[i].strip().split()
            x = int(float(temp[0]))
            y = int(float(temp[1]))
            landmark.append((x,y))
    for point in landmark:
        cv2.circle(image, point, 2, (0,255,0), thickness=-1)
    


"""
i = 1
pathLM = 'annot/' + str(i).zfill(6) + '.pts'
print(pathLM)
with open('annot/000001.pts', 'r') as f:
    data = f.readlines()
    #print(data)
    landmark = []
    #print(data[3])
    #data[3] = data[3].strip('\n')
    #print(data)
    #temp = data[3].split(' ')
    #print(float(temp[1]))
    
    i = 3
    for i in range(3, 71):
        temp = data[i].strip().split()
        x = int(float(temp[0]))
        y = int(float(temp[1]))
        landmark.append((x,y))
        
    print(landmark[0])
"""


def main():
    cap = cv2.VideoCapture('vid.avi')
    fps = cap.get(cv2.CAP_PROP_FPS)
    print('帧率：', fps)
    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    print('总帧数：', total_frames)
    fps_time = int(1000/fps)
    while True:
        ret, img = cap.read()
        frame_index = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
        #print(frame_index)
        plotLM68(img, frame_index)
        cv2.putText(img, 'No.'+str(frame_index), (0,50), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
        cv2.imshow('avi', img)
        if(cv2.waitKey(fps_time) & 0xFF == ord('q')):
            break
    cap.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == '__main__':
    main()
