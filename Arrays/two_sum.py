def two_sum(nums, target):
    """Hash map of value -> index. Time O(n), Space O(n)."""
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []
