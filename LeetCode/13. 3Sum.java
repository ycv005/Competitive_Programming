import java.util.*;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {

        Arrays.sort(nums);
        // its like get a value then call for 2Sum
        List<List<Integer>> a = new ArrayList<List<Integer>>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i == 0 || (i > 0 && nums[i] != nums[i - 1])) {
                int low = i + 1;
                int high = nums.length - 1;
                while (low < high) {
                    int tmp = nums[low] + nums[high] + nums[i];
                    if (tmp > 0) {
                        high--;
                    } else if (tmp < 0) {
                        low++;
                    } else {
                        System.out.println("got a val");
                        a.add(new ArrayList<Integer>(Arrays.asList(nums[i], nums[low], nums[high])));
                        // skipping all duplicates
                        while (low < high && nums[low] == nums[low + 1])
                            low++;
                        while (low < high && nums[high] == nums[high - 1])
                            high--;
                        low++;
                        high--;
                    }
                }
            }
        }
        return a;
    }
}