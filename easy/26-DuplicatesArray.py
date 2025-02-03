nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]

def removeDuplicates(nums):
    curr_unique = 0
    for i in range(0, len(nums)):
        if i==0 or nums[i] != nums[i-1]:
            nums[curr_unique] = nums[i]
            curr_unique += 1
    nums[:] = nums[:curr_unique]
    return len(nums)

removeDuplicates(nums)