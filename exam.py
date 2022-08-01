def func(l1, l2):
    # dp[i][j]: l1[0:i]和l2[0:j]的最长公共子长度
    m, n = len(l1), len(l2)
    dp = [[0] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            if l1[i] == l2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]

l1 = 'abcsd'
l2 = 'ebcsfs'
print(func(l1, l2)) 