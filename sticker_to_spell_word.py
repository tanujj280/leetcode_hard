from functools import lru_cache  
#its wrong solution because we are doing comparision at tar[i] and we are concernd about order
#so state is flawed instead we use the remaining character to solve subproblem see this approach is correct 
# but the stae i am using is flawed
# def x(stickers,target):
#     n=len(stickers)
#     s=stickers
#     # @lru_cache(None)
#     def ind(i):
#         return ord(i)-97
#     def f(i,tab):
#         if i>len(target)-1:
#             return 0

#         elif tab[ind(target[i])]>0:
#             tab[ind(target[i])]-=1
#             return f(i+1,tab)
#         else:
#             mini=float("inf")
#             for j in range(n):
#                 t=[0]*26
#                 for k in s[j]:
#                     t[ind(k)]+=1
#                 if t[ind(target[i])]>0:
#                     for p in range(26):
#                         t[p]+=tab[p]
#                     mini=min(mini,1+f(i+1,t))
#             return mini
#     ans=f(0,[0]*26)
#     return ans if ans!=float("inf") else -1
# print(x(["travel","quotient","nose","wrote","any"],"lastwest"))


# This is same approach just different state
from collections import Counter
def x(stickers,target):
    n = len(stickers)
    sticker_counts = []
    for s in stickers:
        sticker_counts.append(Counter(s))

    @lru_cache(None)
    def dp(remain):
        if not remain:
            return 0
        remain_count = Counter(remain)
        res = float('inf')
        for sticker in sticker_counts:
            if remain[0] not in sticker:
                continue
            # build new remaining string
            new_remain = ''
            for ch in remain_count:
                cnt = remain_count[ch] - sticker[ch]
                if cnt > 0:
                    new_remain += ch * cnt
            temp = dp(new_remain)
            if temp != -1:
                res = min(res, 1 + temp)
        return res if res != float('inf') else -1

    return dp(target)

print(x(["travel","quotient","nose","wrote","any"],"lastwest"))
