
def isAnagram(s, t):
    s = list(s)
    for i in t:
        if i in s:
            s.remove(i)
        else:
            return False
    if len(s) == 0:
        return True
    else:
        return False

s = "anagram"
t = "nagaram"

print(isAnagram(s,t))

# Much more optimised

def isAnagram(s, t):
    return sorted(s) == sorted(t)