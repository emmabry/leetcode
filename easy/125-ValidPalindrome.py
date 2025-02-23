# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Initial solution
def isPalindrome(s):
    letters = "abcdefghijklmnopqrstuvwxyz0123456789"
    string = ""
    for l in s.lower():
        if l in letters:
            string += l
    return string == string[::-1]
    
print(isPalindrome("OP"))