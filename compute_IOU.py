def compute_IOU(rec1, rec2):
    """
    rec1: (x0, y0, x1, y1)
    rec2: (x0, y0, x1, y1)
    """
    xmin = max(rec1[0], rec2[0])
    ymin = max(rec1[1], rec2[1])
    xmax = min(rec1[2], rec2[2])
    ymax = min(rec1[3], rec2[3])

    if(xmin>=xmax or ymin>=ymax):
        return 0
    else:
        s1 = (rec1[2]-rec1[0]) * (rec1[3]-rec1[1])
        s2 = (rec2[2]-rec2[0]) * (rec2[3]-rec2[1])
        corss_s = (xmax-xmin) * (ymax-ymin)
        return corss_s / (s1+s2-corss_s)

#测试样例1
r1=(2,3,10,12)
r2=(12,5,20,24)
IOU = compute_IOU(r1,r2)
print("测试样例1，IOU：%f"%IOU)
#测试样例2
r1=(2,2,4,4)
r2=(3,3,5,5)
IOU = compute_IOU(r1,r2)
print("测试样例2，IOU：%f"%IOU)

# ref: https://zhuanlan.zhihu.com/p/197895548
# ref: https://blog.csdn.net/lrs1353281004/article/details/88534452
