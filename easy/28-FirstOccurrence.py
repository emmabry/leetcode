def firstOccurrence(needle, haystack):
    for i in range(0, len(haystack)):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

haystack = "leetcode"
needle = "leeto"

print(firstOccurrence(needle, haystack)) 