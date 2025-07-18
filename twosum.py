class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inithash ={}
        for i,n in enumerate(nums):
            if target - n in inithash:
                return [inithash[target -n],i]
            inithash[n] = i
        return