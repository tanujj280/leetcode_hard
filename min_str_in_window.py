# def minWindow(s,t):
#     n=len(s)
#     m=len(t)
#     if m==0 or n==0:
#         return ''
#     if m>n:
#         return ""
#     tab=[[0]*52 for _ in range(n+1)]
#     def k(x):
#         if ord(x)>=97:
#             return ord(x)+26-97
#         return ord(x)-65
#     from copy import deepcopy
#     for i in range(1, n+1):
#         tab[i] = deepcopy(tab[i-1])
#         tab[i][k(s[i-1])] += 1
#     a=[0]*52
#     for i in range(m):
#         a[k(t[i])]+=1
#     print(a)
#     i=0
#     j=0

#     for l in range(n):
#         # print(k(s[l]),l,"op")
#         if a[k(s[l])]>0:
#             i=l
#             break

#     j=i
#     ans= [0,n+1]
#     if m==1:
#         if t in s:
#             return t
#         else:
#             return ""
    
#     g=0
#     j=i+1
#     print(i,j)
#     while i<j and j<n:
#         # print(i,j,ans)
#         if a[k(s[i])]==0 and i<j:
#             i+=1
#         if a[k(s[i])]>0:
#             f=1
#             for o in range(52):
#                 if tab[j+1][o]-tab[i][o]<a[o]:
#                     f=0
#                     print(s[i],s[j],i,j)
#                     break
#             if not f:
#                 j+=1
#             else:
                
#                 if ans[1]-ans[0]+1>j-i+1:
#                     ans[0]=i
#                     ans[1]=j
#                     print(ans,"op")
#                 i+=1
#     print(ans)
#     if ans[1]-ans[0]>n:
#         return ""
#     else:
#         res=""
#         for i in range(ans[0],ans[1]+1):
#             res+=s[i]
#         return res

from collections import Counter

def minWindow(s, t):
    if not t or not s:
        return ""
    
    target_count = Counter(t)
    window_count = {}
    
    have, need = 0, len(target_count)
    res = [-1, -1]
    res_len = float("inf")
    l = 0
    
    for r in range(len(s)):
        c = s[r]
        window_count[c] = window_count.get(c, 0) + 1

        if c in target_count and window_count[c] == target_count[c]:
            have += 1

        while have == need:
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1

            window_count[s[l]] -= 1
            if s[l] in target_count and window_count[s[l]] < target_count[s[l]]:
                have -= 1
            l += 1
    
    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""

print(minWindow("adobecodebanc","abc"))