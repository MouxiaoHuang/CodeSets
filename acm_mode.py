
A = [2, 5, 6, 5]
B = [5, 4, 2, 2]
S = 8

def func(A, B, S):
    N = len(A)

    resAB, trackAB = [], []
    visitedA = [0] * N
    visitedB = [0] * N
    resBA, trackBA = [], []

    def backtrackAB(start, trackAB):
        if len(trackAB) == N:
            resAB.append(trackAB[:])
        for i in range(start, N):
            print(A[i], B[i], trackAB)
            if A[i] not in trackAB and not visitedA[i]:
                trackAB.append(A[i])
                visitedA[i] = 1
            elif B[i] not in trackAB and not visitedB[i]:
                trackAB.append(B[i])
                visitedB[i] = 1
            else:
                continue
            backtrackAB(i + 1, trackAB)
            trackAB.pop()
            visitedA[i] = 0
            visitedB[i] = 0
    
    backtrackAB(0, trackAB)
    print(resAB)
    if not resAB:
        return False
    return True

    # def backtrackBA(start, trackBA):
    #     # if len(trackBA) == N:
    #     resBA.append(trackBA[:])
    #     for i in range(start, N):
    #         if B[i] not in trackBA:
    #             trackBA.append(B[i])
    #         elif A[i] not in trackBA:
    #             trackBA.append(A[i])
    #         else:
    #             continue
    #         backtrackBA(i + 1, trackAB)
    #         trackBA.pop()
    
    # backtrackBA(0, trackBA)
    # print(resBA)

print(func(A, B, S))