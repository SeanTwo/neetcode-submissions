class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        leng = len(nums)
        has_dupe = False
        for i in range(0, leng):
            if seen.get(nums[i]) == True:
                has_dupe = True
            else:
                seen[nums[i]] = True
        return has_dupe