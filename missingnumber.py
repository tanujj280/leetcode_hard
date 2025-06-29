def firstMissingPositive(nums):
        n=len(nums)
        c=0
        for i in range(n):
            if nums[i]==1:
                c=1
            elif nums[i]<=0 or nums[i]>n:
                nums[i]=1
        # print(nums)
        if not c:
            return 1
        for i in range(n):
            j=abs(nums[i])
            if j==n:
                nums[0]=-abs(nums[0])
            elif j<n:
                nums[j]=-abs(nums[j])
        # print(nums)
        for i in range(1,n):
            if nums[i]>0:
                return i
        if nums[0]<0:
            return n
print(firstMissingPositive([1]))  # Example usage