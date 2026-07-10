class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Boolean> map = new HashMap<Integer, Boolean>();
        boolean has_duplicate = false;

        for(int i = 0; i<nums.length; i++)
        {
            if(map.get(nums[i]) != null)
            { has_duplicate = true; }
            else
            { map.put(nums[i], true); }
        }
        return has_duplicate;
    }
}