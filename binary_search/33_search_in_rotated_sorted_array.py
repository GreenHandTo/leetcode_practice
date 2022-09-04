# https://leetcode.cn/problems/search-in-rotated-sorted-array/
# 在使用二分法时，mid位置分成的前后两部分，肯定有一部分是有序的，另外一部分可能有序
# 判断出前后两部分哪个有序，根据nums[mid] >= nums[left]判断前半部分有序，否则是后半部分
# 有序，同时判断target如果在有序部分的中间，则继续在有序部分查找，否则在另外一部分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        length = len(nums)
        right = length - 1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target <nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
