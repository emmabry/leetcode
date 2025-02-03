nums = [3,2,2,3]
val = 3

def removeElement(nums, val):
    counter = 0
    for i in range(0, len(nums)):
        if nums[i] != val:
            nums[counter] = nums[i]
            counter += 1
    return counter


print(removeElement(nums, val))