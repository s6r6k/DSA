class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        first = 0
        last = len(s) - 1
        while(first<last):
            char2 = s[last]
            s[last] = s[first]
            s[first] = char2
            first+=1
            last-=1
        return s
        