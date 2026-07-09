class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng = len(nums)
        my_map = {}
        for i in range (0, leng):
            if my_map.get(target-nums[i]) != None:
                return [my_map.get(target-nums[i]), i]
            my_map[nums[i]] = i