class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        Map<Character, Integer> w1 = new HashMap<>();
        Map<Character, Integer> w2 = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (w1.containsKey(s.charAt(i))) { 
                w1.put(s.charAt(i), w1.get(s.charAt(i)) + 1);
            } else { 
                w1.put(s.charAt(i), 1);
            }
            if (w2.containsKey(t.charAt(i))) { 
                w2.put(t.charAt(i), w2.get(t.charAt(i)) + 1);
            } else { 
                w2.put(t.charAt(i), 1);
            }
        }

        return w1.equals(w2);
    }
}
