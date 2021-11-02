def solution(nums):
    new = set(nums)

    if len(nums) // 2 >= len(new):
        return len(new)
    else:
        return len(nums) // 2


solution([1, 1, 1, 1])
