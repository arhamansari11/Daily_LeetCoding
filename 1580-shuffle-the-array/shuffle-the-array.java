class Solution {
    public int[] shuffle(int[] nums, int n) {
        int len = nums.length;
        int [] ans = new int [len];
        for(int i = 0; i < n; i++){
            ans[2*i] = nums[i];
            ans[2*i + 1] = nums[i + n];
        }
        return ans;
    }
}