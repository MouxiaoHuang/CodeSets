# Ref: https://blog.csdn.net/qq_37828488/article/details/100024924

txtfile = 'txt.txt'

with open(txtfile, 'w') as f:
    f.write('test for txt')

with open(txtfile, 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        print(line)