class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        ans = []

        for i in range(len(nums)):
            a = nums[i]
            b = target - a

            if b in h:
                ans.append(h[b])
                ans.append(i)
                return ans
            
            h[a] = i
        
        return ans
