# from functools import lru_cache

# def minimize_max_partition(nums, k):
#     n = len(nums)
    
#     # Prefix sum
#     pre = [0] * (n + 1)
#     for i in range(1, n + 1):
#         pre[i] = pre[i - 1] + nums[i - 1]

#     @lru_cache(None)
#     def f(i, p):
#         if p == k:
#             if i == n:
#                 return 0  # all elements used in k parts
#             else:
#                 return float('inf')  # too few partitions

#         res = float('inf')
#         for j in range(i + 1, n + 1):
#             part_sum = pre[j] - pre[i]
#             res = min(res, max(part_sum, f(j, p + 1)))
#         return res

#     return f(0, 0)

from functools import lru_cache

def minimize_max_partition(nums, k):
    n = len(nums)
    pre = [0] * (n + 1)
    for i in range(1, n + 1):
        pre[i] = pre[i - 1] + nums[i - 1]

    @lru_cache(None)
    def f(i, l, p, val):
        if p == k - 1:
            if i>=n:
                return float("inf")
            return max(val, pre[n] - pre[i])
        if i >= n:
            return float('inf')

        val1 = max(val, pre[i + 1] - pre[l])
        par = f(i + 1, i + 1, p + 1, val1)
        no_par = f(i + 1, l, p, val)
        return min(par, no_par)

    return f(0, 0, 0, 0)

print(minimize_max_partition([7, 2, 5, 10, 8],4))
