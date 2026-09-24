class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int curr = nums[i];
            if(map.containsValue(curr)) return true;
            map.put(i, curr);
        }
        return false;
    }
}