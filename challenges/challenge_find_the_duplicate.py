def find_duplicate(nums):
    if isinstance(nums, list) is False:
        return False
    nums.sort()
    setOfNums = set()
    for num in nums:
        if isinstance(num, int) is False or num < 0:
            return False
        if num in setOfNums:
            return num
        else:
            setOfNums.add(num)
    return False
