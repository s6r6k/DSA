class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in range(len(strs)):
            word = strs[i]
            sWord = "".join(sorted(word))
            if sWord in dict:
                (dict[sWord]).append(word)
            else:
                dict[sWord] = [word]
        return [val for key, val in dict.items()]
        