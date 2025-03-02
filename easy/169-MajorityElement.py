# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums):
    nums_hash = {}
    for n in nums:
        if n not in nums_hash.keys():
            nums_hash[n] = 1
        else:
            nums_hash[n] += 1
        return max(nums_hash, key=nums_hash.get)
    
    
nums = [2,2,1,1,1,2,2]

print(majorityElement(nums))