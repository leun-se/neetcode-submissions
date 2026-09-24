class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()) return false;

        HashMap<Character, Integer> fStr = new HashMap<>();
        HashMap<Character, Integer> sStr = new HashMap<>();

        for(int i = 0; i < s.length(); i++){
            char curr = s.charAt(i);
            if(fStr.containsKey(curr)){
                fStr.put(curr, fStr.get(curr) + 1);
            } else{
                fStr.put(curr, 1);
            }
        }
        for(int i = 0; i < t.length(); i++){
            char curr = t.charAt(i);
            if(sStr.containsKey(curr)){
                sStr.put(curr, sStr.get(curr) + 1);
            } else{
                sStr.put(curr, 1);
            }
        }
        return fStr.equals(sStr);
    }
}
