# https://leetcode.com/problems/search-insert-position/description/

nums = [1,3,5,6,7,11,13]
target = 8


def bsearch1(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left




print(bsearch1(0, len(nums)-1, target))
