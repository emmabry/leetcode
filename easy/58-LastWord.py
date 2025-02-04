# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

s = "   fly me   to   the moon  "

def lengthOfLastWord(s):
    return len(s.strip().split(" ")[-1])

print(lengthOfLastWord(s))