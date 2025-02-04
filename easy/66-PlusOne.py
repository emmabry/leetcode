# You are given a large integer represented as an integer array digits, 
# where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. 
# The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

digits = [9,9,9,9]

# Initial workings (inefficient)

def plusOne(digits):
    num = (int(''.join(map(str, digits))) + 1)
    return [int(i) for i in str(num)]
    
print(plusOne(digits))

# Optimised version 

def plusOne(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits

print(plusOne(digits))