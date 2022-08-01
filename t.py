
in_time = []
out_time = []
pre = ''

def calculate(s_in, s_out):
    a = int(s_out[0:2]) - int(s_in[0:2])
    b = int(s_out[3:5]) - int(s_in[3:5])
    c = int(s_out[6:8]) - int(s_in[6:8])
    if c < 0:
        c = 60 + c
        b = b - 1
    if b < 0:
        b = 60 + c
        a = a - 1
    res = ''
    if a < 10:
        res = '0' + str(a)
    else:
        res = str(a)
    if b < 10:
        res = res + ':0' + str(b)
    else:
        res = res + ':' + str(b)
    if c < 10:
        res = res + ':0' + str(c)
    else:
        res = res + ':' + str(c)
    return res

def cal_sum(s1, s2):
    a = int(s1[0:2]) + int(s2[0:2])
    b = int(s1[3:5]) + int(s2[3:5])
    c = int(s1[6:8]) + int(s2[6:8])
    if c >= 60:
        c = c - 60
        b += 1
    if b >= 60:
        b = b - 60
        a += 1
    res = ''
    if a < 10:
        res = '0' + str(a)
    else:
        res = str(a)
    if b < 10:
        res = res + ':0' + str(b)
    else:
        res = res + ':' + str(b)
    if c < 10:
        res = res + ':0' + str(c)
    else:
        res = res + ':' + str(c)
    return res


n = int(input())
for _ in range(n):
    s = input().split()
    if s[0] == 'out':
        if not in_time or pre == 'out':
            continue
        else:
            out_time.append(s[1])
            pre = 'out'
    elif s[0] == 'in':
        if pre == 'in':
            continue
        else:
            in_time.append(s[1])
            pre = 'in'
# print(in_time)
# print(out_time)
sum_time = []
for i in range(len(in_time)):
    sum_time.append(calculate(in_time[i], out_time[i]))

while True:
    if len(sum_time) == 1:
        break
    else:
        sum_time[1] = cal_sum(sum_time[0], sum_time[1])
        sum_time.pop(0)
print(sum_time[0])