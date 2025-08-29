def two_sum(n, k):
    """正序增长的数组,求两数之和等于k的数的索引位置
    >>> two_sum([2, 7, 11, 15], 9)
    [1, 2]
    >>> two_sum([2, 3, 4, 6, 8], 9)
    [2, 4]
    """
    i, j = 0, len(n) - 1
    while True:
        if n[i] + n[j] == k:
            return [i + 1, j + 1]
        elif n[i] + n[j] > k:
            j -= 1
        elif n[i] + n[j] < k:
            i += 1


def three_sum(nums):
    """返回数组中所有和为0且不重复的三元组
    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    """
    nums = sorted(nums)
    ans = []
    n = len(nums)
    for i in range(n - 2):
        x = nums[i]
        if i > 0 and x == nums[i - 1]:
            continue
        if x + nums[-1] + nums[-2] < 0:
            continue
        if x + nums[i + 1] + nums[i + 2] > 0:
            break
        j = i + 1
        k = n - 1
        while j < k:
            s = x + nums[j] + nums[k]
            if s > 0:
                k -= 1
            elif s < 0:
                j += 1
            else:
                ans.append([x, nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                k -= 1
                while k > j and nums[k] == nums[k + 1]:
                    k -= 1

    return ans
