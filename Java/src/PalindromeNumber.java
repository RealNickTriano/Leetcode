public class PalindromeNumber {
    public static void main(String[] args) {
        assert !isPalindrome(420);
        assert !isPalindrome(-121);
        assert isPalindrome(121);
        assert !isPalindrome(10);
    }

    public static boolean isPalindrome(int x) {
        // Convert to String Builder
        StringBuilder preReversed = new StringBuilder(String.valueOf(x));
        // Reverse String Builder
        StringBuilder reversed = new StringBuilder(String.valueOf(x)).reverse();
        // Check if equal pre-reversed
        return preReversed.compareTo(reversed) == 0;
    }
}
