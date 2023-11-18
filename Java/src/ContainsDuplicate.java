import java.util.*;
import java.util.stream.Collectors;

public class ContainsDuplicate {
    public static void main(String[] args) {
        System.out.println(containsDuplicate(new int[]{1,2,3,1}));
        System.out.println(containsDuplicate(new int[]{1,2,3,4}));
        System.out.println(containsDuplicate(new int[]{1,1,1,3,3,4,3,2,4,2}));
    }

    public static boolean containsDuplicate(int[] nums) {
        Set mySet = new HashSet<Integer>();
        for (int i = 0; i < nums.length; i++) {
            mySet.add(nums[i]);
        }
        return nums.length != mySet.size();
    }
}
