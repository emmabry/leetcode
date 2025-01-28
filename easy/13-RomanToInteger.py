# Given a Roman numeral, convert it to an integer

def romanToInt(s):
    numerals = { 'I': 1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    
    total = 0
    for i in range(len(s)):
        if i + 1 < len(s) and numerals[s[i]] < numerals[s[i + 1]]:
            # Numerals are always ascending in order unless its IX, CM etc, where it needs to be subtracted
            total -= numerals[s[i]]
        else:
            total += numerals[s[i]]
    return total

s = "MMCCCXCIX"

print(romanToInt(s))