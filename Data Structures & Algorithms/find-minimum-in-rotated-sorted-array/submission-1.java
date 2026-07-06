class Solution {
    public int findMin(int[] nums) {
        int result = Integer.MAX_VALUE;
        int lo = 0;
        int hi = nums.length - 1;

        while (lo <= hi) {
            if (nums[lo] <= nums[hi]) {
                result = Math.min(result, nums[lo]);
                break;
            }

            int mid = lo + (hi - lo) / 2;
            result = Math.min(result, nums[mid]);
            if (nums[lo] <= nums[mid]) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return result;
    }
}
