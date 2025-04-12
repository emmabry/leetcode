def containsNearbyDuplicate(nums, k):
    pointer = 0
    if len(nums) == len(set(nums)):
        return False
    for i in nums:
        for i in range(1, k+1):
            print(f"pointer is {pointer} and i is {i}")
            if pointer + i >= len(nums):
                continue
            elif nums[pointer] == nums[pointer+i]:
                return True
        pointer +=1
    return False

nums = [1,2,3]
k = 2


print(containsNearbyDuplicate(nums, k))