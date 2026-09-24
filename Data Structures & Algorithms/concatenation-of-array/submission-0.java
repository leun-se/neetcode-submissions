class Solution {
    public int[] getConcatenation(int[] nums) {
        int origLength = nums.length;
        int[] ans = new int[origLength*2];
        for(int i = 0; i < ans.length; i++){
            if(i < origLength){
                ans[i] = nums[i];
            } else{
                ans[i] = nums[i-origLength];
            }
        }
        return ans;
    }
}