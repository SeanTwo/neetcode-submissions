class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        leng = len(nums)
        tar = sum(list(range(1,leng+1)))
        return tar - sum(nums)