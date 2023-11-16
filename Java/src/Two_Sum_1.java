import java.util.HashMap;

public class Two_Sum_1 {
    public static void main(String[] args) {

    }
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> targets = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            if (targets.get(nums[i]) == null) {
                targets.put(target - nums[i], i);
            } else {
                return new int[]{targets.get(nums[i]), i};
            }
        }

        // Has exactly one solution so won't happen
        return null;
    }
}
