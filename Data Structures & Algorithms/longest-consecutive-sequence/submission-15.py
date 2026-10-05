class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestSeqLen = 0

        for n in nums:
            if (n-1) not in numsSet:
                seqLen = 0
                while (n + seqLen) in numsSet:
                    seqLen += 1
                longestSeqLen = max(seqLen, longestSeqLen)

        return longestSeqLen