def trap(height):
    """给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
    下雨之后能接多少雨水。
    https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png
    >>> height = [0,1,0,2,1,0,1,3,2,1,2,1]
    >>> trap(height)
    6
    """
    n = len(height)

    pre_max = [0] * n
    pre_max[0] = height[0]
    for i in range(1, n):
        pre_max[i] = max(height[i], pre_max[i - 1])

    suf_max = [0] * n
    suf_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        suf_max[i] = max(height[i], suf_max[i + 1])

    ans = 0
    for h, pre, suf in zip(height, pre_max, suf_max):
        ans += min(pre, suf) - h

    return ans


def trap2(height):
    """给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，
    下雨之后能接多少雨水。
    双指针左右靠近
    https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png
    >>> height = [0,1,0,2,1,0,1,3,2,1,2,1]
    >>> trap(height)
    6
    """
    ans = 0
    left, right = 0, 0
    pre_max, suf_max = 0, 0
    while left <= right:
        pre_max = max(pre_max, height[left])
        suf_max = max(suf_max, height[right])
        if pre_max < suf_max:
            ans += pre_max - height[left]
            left += 1
        else:
            ans += suf_max - height[right]
            right -= 1

    return ans
