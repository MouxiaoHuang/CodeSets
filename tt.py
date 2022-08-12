# 目标第k大的数字
import random

nums = [0, 9, 72, 3, 2, 98, 7, 18, 87]
k = 3

def quick_sort(nums):
    def partition(nums, low, high):
        pivot_idx = random.randint(low, high)
        
        nums[pivot_idx], nums[low] = nums[low], nums[pivot_idx]
        pivot = nums[low]

        left, right = low, high
        while left < right:
            # 右边第一个大于pivot
            while left < right and nums[right] >= pivot:
                right -= 1
            nums[left] = nums[right]
            
            while left < right and nums[left] <= pivot:
                left += 1
            nums[right] = nums[left]
        nums[left] = pivot
        return left

    def qs(nums, low, high):
        if low >= high:
            return
        mid = partition(nums, low, high)
        qs(nums, 0, mid - 1)
        qs(nums, mid + 1, high)
    qs(nums, 0, len(nums) - 1)
    return nums
res = quick_sort(nums)
res.reverse()
print(res, k)
print(res[k])