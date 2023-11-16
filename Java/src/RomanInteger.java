import java.util.HashMap;

public class RomanInteger {
    public static void main(String[] args) {

    }

    public static int romanToInt(String s) {
        HashMap<Character, Integer> romanToIntTable =
                new HashMap<>();
        romanToIntTable.put('I', 1);
        romanToIntTable.put('V', 5);
        romanToIntTable.put('X', 10);
        romanToIntTable.put('L', 50);
        romanToIntTable.put('C', 100);
        romanToIntTable.put('D', 500);
        romanToIntTable.put('M', 1000);

        int total = 0;
        for(int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1 &&
                    romanToIntTable.get(s.charAt(i)) < romanToIntTable.get(s.charAt(i + 1))) {
                total -= romanToIntTable.get(s.charAt(i));
            } else {
                total += romanToIntTable.get(s.charAt(i));
            }
        }

        return total;
    }
}
