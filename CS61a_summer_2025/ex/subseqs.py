MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"


def letterCombinations(digits):
    """
    >>> print(letterCombinations("23"))
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    """
    n = len(digits)
    if n == 0:
        return []
    ans = []
    path = [""] * n

    def dfs(i):
        if i == n:
            ans.append("".join(path))
            return
        for c in MAPPING[int(digits[i])]:
            path[i] = c
            dfs(i + 1)

    dfs(0)

    return ans


def subseqs(s):
    """Return a nested list (a list of lists) of all subsequences of S.
    The subsequences can appear in any order. You can assume S is a list.

    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    n = len(s)
    ans = []
    path = []

    def dfs(i):
        if i == n:
            ans.append(path.copy())
            return

        dfs(i + 1)
        path.append(s[i])
        dfs(i + 1)
        path.pop()

    dfs(0)
    return ans
