class Solution {
    public int removeElement(int[] nums, int val) {
        int last = nums.length-1;
        int k = 0;
        for (int i = 0; i <= last - k; i++) {
            if (nums[i] == val) {
                while (last - k >= 0 && nums[last - k] == val) {
                    k++;
                }
                if (i <= last - k) {
                    nums[i] = nums[last - k];
                    k++;
                }
            }
        }
        return (last+1)-k;
    }
}