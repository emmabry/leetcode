# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

nums = [1,3,5,6]
target = 0

def searchInsert(nums, target):
    middle = len(nums) // 2
    if nums[middle] == target or (middle == 0 and nums[middle] > target):
        return middle
    elif nums[middle] < target and (middle == len(nums)-1 or nums[middle+1] > target):
        return middle+1
    elif nums[middle] > target and nums[middle-1] < target:
        return middle
    elif nums[middle] > target:
        return searchInsert(nums[:middle], target)
    elif nums[middle] < target:
        return middle + searchInsert(nums[middle:], target)

print(searchInsert(nums, target))