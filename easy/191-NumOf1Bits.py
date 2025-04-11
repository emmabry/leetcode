def hammingWeight(n):
    count = 0
    for i in str(bin(n))[2:]:
        if i == '1':
            count += 1
    return count 
