class Solution {
    public int lengthOfLongestSubstring(String s) {
        int longest = 0;
        HashSet<Character> set = new HashSet<>();
        int l = 0;
        int r = 0;

        while (r < s.length()) {
            while (set.contains(s.charAt(r))) {
                set.remove(s.charAt(l));
                l++;
            }

            set.add(s.charAt(r));
            longest = Math.max(longest, r - l + 1);
            r++;
        }

        return longest;
        
    }
}
