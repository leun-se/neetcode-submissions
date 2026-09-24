class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            map.merge(nums[i], 1, Integer::sum);
        }
         Map.Entry<Integer, Integer> maxEntry = map.entrySet().stream().max(Map.Entry.comparingByValue()).get();

        return maxEntry.getKey();
    }
}