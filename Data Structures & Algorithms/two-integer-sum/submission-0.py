class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i,n in enumerate(nums):
            if (target-n) in hashtable.keys():
                return [hashtable[target-n],i]
            else:
                hashtable[n]=i

        