class Solution {
    public int lengthOfLIS(int[] arr) {
        int[] arr = { 10, 22, 9, 3, 21, 50, 41, 60, 80 };
        int[] dp = new int[arr.length];
        Arrays.fill(dp, 1);

        for (int i = 1; i < arr.length; i++) {
            int mx = Integer.MIN_VALUE;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    mx = Math.max(mx, dp[j]);
                }
            }
            if (mx == Integer.MIN_VALUE) {
                mx = 0;
            }
            dp[i] = mx + 1;
        }
        int newmx = Integer.MIN_VALUE;
        for (int i = 0; i < dp.length; i++) {
            newmx = Math.max(newmx, dp[i]);
        }
        return newmx;
    }
}