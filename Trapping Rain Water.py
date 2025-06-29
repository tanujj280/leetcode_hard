def trap(height):
    from collections import deque
    n=len(height)
    ind=n
    for i in range(n):
        if height[i]>0:
            if i+1<n and  height[i+1]-height[i]<0:
                ind=i
                break
    if ind==n:
        return 0
    q=deque()
    q.append((height[ind],1))
    ans=0
    for i in range(ind,n):
        l=1
        if height[i]>q[0][0]:
            th,lenn=q.popleft()
            while q:
                j,x=q.popleft()
                ans+=(th-j)*x
                lenn+=x
            l=lenn
        else:
            while q and height[i]>=q[-1][0]:
                length=q[-1][1]
                j=q[-1][0]
                th=height[i]
                ans+=(th-j)*length
                l+=length
                q.pop()
        q.append((height[i],l))
    return ans

print(trap([0]))
