def twoSum(nums, target):
        hash_map = {index: val for val, index in enumerate(nums)}
        for i in range(len(nums)):
            search_value = target - nums[i]
            if search_value in hash_map and hash_map[search_value] != i:
                return [i, hash_map[search_value]]