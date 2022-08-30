# n = int(input())
n = 4
# times = [[1, 2], [2, 3]]
# times = [[1, 3], [2, 4]]
times = [[1, 2], [2, 3], [3, 4], [3, 8]]


def process_input():
    n = int(input())
    tmp = input().split(' ')
    times = []
    for i in range(0, len(tmp), 2):
        time = [int(tmp[i]), int(tmp[i + 1])]
        times.append(time)
    return n, times


def solution(n, times):
    times.sort(key=lambda x: x[0])
    res = []
    c = 1
    for tmp in times:
        if not res or tmp[0] >= res[-1][1]:
            res.append(tmp)
        else:
            res[-1][1] = max(res[-1][1], tmp[1])
            c += 1
    # print(len(res))
    print(res, c)
    return len(res)


# n, times = process_input()
print(solution(n, times))
