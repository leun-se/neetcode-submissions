class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        
        // loop over each word
        for (int i = 0; i < strs.length; i++) {
            String val = strs[i];
            char[] cur = val.toCharArray();

            // sort them to be consistent, then convert into String
            Arrays.sort(cur);
            String key = new String(cur);

            if (map.containsKey(key)){
                List<String> str = map.get(key);
                str.add(new String(val));
            } else {
                List<String> str = new ArrayList<String>();
                str.add(new String(val));
                map.put(key, str);
            }
            
        }
        return new ArrayList<List<String>>(map.values());
    }
}
