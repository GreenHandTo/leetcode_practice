# 三数之和：https://leetcode.cn/problems/3sum/submissions/
# 该题还能用双指针来解决
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 避免重复
        length = len(nums)
        hash_dict = {nums[i]: i for i in range(length)}
        ret = []

        for i in range(length):
            if i != 0 and nums[i] == nums[i-1]:  # 避免重复
                continue
            for j in range(i+1, length):
                if j != i + 1 and nums[j] == nums[j-1]:
                    continue
                c = -1 * (nums[i] + nums[j])
                if c in hash_dict and hash_dict[c] > j:  # >j为避免重复
                    ret.append([nums[i], nums[j], c])
        return ret