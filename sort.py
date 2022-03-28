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



from xml.dom import minidom


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