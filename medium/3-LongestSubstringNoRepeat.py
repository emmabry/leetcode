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

# Sliding Window
def lengthOfLongestSubstring(s):
    left = 0
    maxLen = 0
    charset = set()
    for i in range(len(s)):
        while s[i] in charset:
           charset.remove(s[left])
           left += 1
        charset.add(s[i])
        maxLen = max(maxLen, i - left + 1)
    return maxLen

s = "dvdf"

print(lengthOfLongestSubstring(s))