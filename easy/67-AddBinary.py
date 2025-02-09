# Given two binary strings a and b, return their sum as a binary string.

a = "1111"
b = "1111"

# Inefficient starting attempt

def addBinary(a, b):
    carry = 0
    ret = []
    if len(a) > len(b):
        longer = a
        shorter = b
    else:
        longer = b
        shorter = a
    i = 1
    while i < len(longer) + 1:
        if len(shorter) < i:
            if int(longer[-i]) + carry == 0:
                ret.insert(0, '0')
                carry = 0
            elif int(longer[-i]) + carry == 1:
                ret.insert(0, '1')
                carry = 0
            elif int(longer[-i]) + carry == 2:
                ret.insert(0, '0')
                carry = 1
        else:
            if int(longer[-i]) + int(shorter[-i]) + carry == 0:
                ret.insert(0, '0')
                carry = 0
            elif int(longer[-i]) + int(shorter[-i]) + carry == 1:
                ret.insert(0, '1')
                carry = 0
            elif int(longer[-i]) + int(shorter[-i]) + carry == 2:
                ret.insert(0, '0')
                carry = 1
            elif int(longer[-i]) + int(shorter[-i]) + carry == 3:
                ret.insert(0, '1')
                carry = 1
        i += 1
    if carry == 1:
        if int(longer[0]) + int(shorter[0]) + int(ret[0]) == 3:
            ret[0] = '1'
        elif ret[0] == '1':
            ret[0] = '0'
        ret.insert(0, '1')

    return ''.join(ret)

# Efficient solution:
def addBinary(a,b):
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))
    
print(addBinary(a,b))