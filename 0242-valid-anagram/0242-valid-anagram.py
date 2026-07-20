class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for c in list(s):
            if c in dict:
                dict[c] += 1
            else:
                dict[c] = 1
        for c in list(t):
            if c not in dict:
                return False
            else:
                dict[c] -=1
        for val in dict.values():
            if val != 0:
                return False
        return True
        