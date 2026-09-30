class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        arr = []

        for i in range(len(nums)):
            a = nums[i]
            b = target - a

            if b in h:
                arr.append(h[b])
                arr.append(i)
                return arr
            
            h[a] = i
        
        return arr
