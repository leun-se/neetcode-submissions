class Solution {
    public String longestCommonPrefix(String[] strs) {

        StringBuilder substring = new StringBuilder("");
        String match = strs[0];

        for (int i = 0; i < match.length(); i++){
            for(int j = 1; j < strs.length; j++){
                String curr = strs[j];
                if(curr.length() < i+1) return substring.toString();
                if(match.charAt(i) != curr.charAt(i)) return substring.toString();
            }
            substring.append(match.charAt(i));
        }
        return match;
    }
}