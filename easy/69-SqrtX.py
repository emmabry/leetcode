# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
# The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

x = 8

def mySqrt(x):
    if x == 0:
        return 0
    else:
        # Binary search
        def binarySearchSum(x, left, right):
            mid = (left + right) // 2
            
            if mid * mid < x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid == x:
                return mid
            elif mid * mid < x:
                return binarySearchSum(x, mid+1, right)
            else:
                return binarySearchSum(x, left, mid-1)
        
        return binarySearchSum(x, 0, 999999)
    
print(mySqrt(x))