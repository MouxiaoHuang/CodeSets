# 以下数组中存放的是随时间变化的股价，你可以在其中选择一个买入点，并选择一个卖出点，
# 使得收益达到最大，注意卖出点需要在买入点之后，请使用你最熟悉的编程语言实现该算法。
# 你可以编写一个函数，函数的输入为股价数组，输出为买入点和卖出点的index。
#       [4, 3, 6, 1, 3, 5, 8, 3, 9, 6]

nums = [4, 3, 6, 1, 3, 5, 8, 3, 9, 6]

def max_price(nums):
    '''input: nums
       output: [买入的天数index，卖出的index]
    '''
    MAX = 0
    res = [0, 0]
    for i in range(0, len(nums) - 1, 1):
        for j in range(i + 1, len(nums), 1):
            # 表明，第j天卖出、第i天买入的收益大于之前的最大收益，所以更新
            if nums[j] - nums[i] > MAX:
                MAX = nums[j] - nums[i]
                res = [i, j]
    return res

print(max_price(nums))

def func_On(nums):
    '''input: nums
       output: [买入的天数index，卖出的index]
    '''
    MIN, MAX = float('inf'), 0
    res = [0, 0]

    for i in range(len(nums)):
        if nums[i] < MIN:
            MIN = nums[i]
            res[0] = i
        tmp_MAX = nums[i] - MIN
        if tmp_MAX > MAX:
            MAX = tmp_MAX
            res[-1] = i
    return res

print(func_On(nums))