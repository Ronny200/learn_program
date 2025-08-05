def maxArea(height):
    """给定一个长度为n的数组height,有n条垂线,第i条线的两个端点
    是(i, 0) and (i, height[i])，找出两条线让他们构成的容积可以
    容纳最多的水（高度为数组中的值，宽度为两条线索引的差）
    >>> maxArea([1,8,6,2,5,4,8,3,7])
    49
    """
    ans = 0
    left = 0
    right = len(height) - 1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        ans = max(ans, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return ans
