class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        count = 1
        maxCount = 1

        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i] + 1:
                count += 1
                maxCount = max(count, maxCount)
            elif nums[i+1] == nums[i]:
                continue
            else:
                count = 1
                continue

        return maxCount