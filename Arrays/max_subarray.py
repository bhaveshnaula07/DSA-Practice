#LeetCode 53, Medium, Kadane's)
def max_subarray(nums):
    """Time O(n), Space O(1)."""
    best = cur = nums[0]
    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)
    return best
