# Brute Force
def lengthOfLongestSubstring(s):
    maxLen = 0
    for i in range(len(s)):
        if maxLen == 95:
            return maxLen
        n = len(s)
        while n>i:
            if len(s[i:n]) == len(''.join(set(s[i:n]))):
                if len(s[i:n]) > maxLen:
                    maxLen = len(s[i:n])
            n -= 1
    return maxLen
    

s = "dvdf"

print(lengthOfLongestSubstring(s))