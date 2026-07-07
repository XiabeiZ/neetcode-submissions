class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int l = 0;
        int r = 0;

        while (r < prices.length) {
            if (prices[r] > prices[l]) {
                res = Math.max(res, prices[r] - prices[l]);
            } else {
                l = r;
            }
            r++;
        }

        return res;

    }
}
