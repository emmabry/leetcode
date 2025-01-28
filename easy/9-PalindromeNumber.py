# Given an integer x, return true if x is palindrome integer, false otherwise.

def isPalindrome(x):
    return str(x) == str(x)[::-1]
