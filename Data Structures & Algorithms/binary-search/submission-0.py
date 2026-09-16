class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lb = 0 # lower bound
        ub = len(nums)-1 # upper bound
        while(lb <= ub):
            mid = lb + (ub-lb) // 2
            if(target < nums[mid]): # Target is lower than the middle
                ub = mid - 1
            else:
                lb = mid + 1
            mid = lb + (ub-lb) // 2
        mid = -1 if nums[mid] != target else mid
        return mid
        