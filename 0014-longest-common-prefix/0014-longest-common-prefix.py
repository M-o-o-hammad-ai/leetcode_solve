class Solution(object):
   def longestCommonPrefix(self,strs):
    if not strs:
        return ""

    minLen = min(len(s) for s in strs)
    prefix = ""
    for i in range(minLen):
        char = strs[0][i]
        if all(s[i] == char for s in strs):
            prefix += char
        else:
            break

    return prefix
        