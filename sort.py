# # ref: https://zhuanlan.zhihu.com/p/57270323 &
# # https://blog.csdn.net/weixin_41571493/article/details/81875088

# def bubblesort(nums):
#     for i in range(len(nums)-1):
#         for j in range(len(nums)-i-1):
#             if nums[j]>nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums

# def selectsort(nums):
#     for i in range(len(nums)-1):
#         min = nums[i]
#         for j in range(i+1, len(nums)):
#             if nums[j]<min:
#                 min = nums[j]
#                 nums[i], nums[j] = nums[j], nums[i]
#     return nums

# def insertsort(nums):
#     for i in range(1, len(nums)):
#         j = i-1
#         key = nums[i]
#         while j>=0:
#             if nums[j]>key:
#                 nums[j+1] = nums[j]
#                 nums[j] = key
#             j -= 1
#     return nums

# def quicksort(nums):
#     def partition(nums, left, right):
#         key = left
#         while left<right:
#             while left<right and nums[right]>=nums[key]:
#                 right -= 1
#             while left<right and nums[left]<=nums[key]:
#                 left += 1
#             nums[left], nums[right] = nums[right], nums[left]
#         nums[left], nums[key] = nums[key], nums[left]
#         return left
#     def qs(nums, left, right):
#         if left>=right:
#             return
#         mid = partition(nums, left, right)
#         qs(nums, left, mid-1)
#         qs(nums, mid+1, right)
#     n = len(nums)
#     if n<=1:
#         return nums
#     qs(nums, 0, n-1)
#     return nums


# if __name__ == '__main__':
#     nums = [6,8,3,2,9,1]
#     print(bubblesort(nums))
#     print(selectsort(nums))
#     print(insertsort(nums))
#     print(quicksort(nums))



from random import random
from turtle import right


def bubblesort(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j+1] < nums[j]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def selectsort(nums):
    for i in range(len(nums) - 1):
        MIN = nums[i]
        for j in range(i+1, len(nums)):
            if nums[j] <= MIN:
                MIN = j
                nums[j], nums[i] = nums[i], nums[j]
    return nums

def insertsort(nums):
    for i in range(1, len(nums) - 1):
        key = nums[i]
        j = i - 1
        while j:
            if nums[j] > key:
                nums[j + 1] = nums[j]
                nums[j] = key
            j -= 1
    return nums

nums = [6,8,3,2,9,1]
print(bubblesort(nums))
print(selectsort(nums))
print(insertsort(nums))


def quicksort(nums):
    def partition(nums, left, right):
        key = left
        while left < right:
            while left < right and nums[right] >= nums[key]:
                right -= 1
            while left < right and nums[left] <= nums[key]:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[key] = nums[key], nums[left]
        return left
    def qs(nums, left, right):
        if left >= right:
            return
        mid = partition(nums, left, right)
        qs(nums, left, mid - 1)
        qs(nums, mid + 1, right)
    n = len(nums)
    if n<=1:
        return nums
    qs(nums, 0, n-1)
    return nums

'''默写
'''
def quicksort_randpivot(nums):
    def partition(nums, low, high):
        pivot_idx = random.randint(low, high) # 随机选择pivot
        nums[pivot_idx], nums[low] = nums[low], nums[pivot_idx] # 把pivot放到最左边
        pivot = nums[low] # 选取最左边为pivot

        left, right = low, high
        while left < right:
            while left < right and nums[right] >= pivot: # 找到右边第一个<pivot的元素
                right -= 1
            nums[left] = nums[right] # 并将其移动到left处
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left
    
    def quicksort(nums, low, high):
        if low >= high:
            return
        mid = partition(nums, low, right) 
        quicksort(nums, 0, mid - 1)
        quicksort(nums, mid + 1, high)
    quicksort(nums, 0, len(nums) - 1)
    return nums

'''默写
'''
def mergesort(nums, low, high):
    if low >= high:
        return
    # divide / conquer
    # 求中点，分为前后两段，排序
    mid = low + (high - low) // 2
    mergesort(nums, low, mid)
    mergesort(nums, mid + 1, high)

    # combine
    # 用两个指针指向前后两段
    left, right = low, mid + 1
    tmp = []
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            tmp.append(nums[left])
            left += 1
        else:
            tmp.append(nums[right])
            right += 1
    # 若左 / 右还有剩余，则添加到后面去
    while left <= mid:
        tmp.append(nums[left])
        left += 1
    while right <= high:
        tmp.append(nums[right])
        right += 1

    nums[low:high + 1] = tmp # 对low:high区间排序完了
    return nums

print('mergesort: ', mergesort(nums, 0, len(nums) - 1))
