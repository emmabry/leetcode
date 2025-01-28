# Write a function to find the longest common prefix amongst an array of strings
# If no common prefix, return ""

def longestCommonPrefix(strs):
    if len(strs) == 1:
        return strs[0]

    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for word in strs:
            if word[i] != char:
                return shortest[:i]
    return shortest
