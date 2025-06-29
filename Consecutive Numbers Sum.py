def consecutiveNumbersSum(n):
    # i=1
    # ans=0
    # while i//2<(n//i):
    #     if n%i==0:
    #         ans+=1
    #         # print(i)
    #     i+=2
    # j=2
    # while n%j==j//2 and j//2-1<(n//j):
    #     ans+=1
    #     j+=2
    # return ans
    x=1
    ans=0
    while n>=x*(x+1)//2 :
        if (n-x*(x+1)//2)%x==0:
            ans+=1
        x+=1
    return ans

print(consecutiveNumbersSum(15))
