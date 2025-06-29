def findMedianSortedArrays(num1, num2):
    # Ensure num1 is the smaller array
    if len(num1) > len(num2):
        num1, num2 = num2, num1

    n, m = len(num1), len(num2)
    total = n + m
    half = total // 2

    l, r = 0, n
    while l <= r:
        mid1 = (l + r) // 2
        mid2 = half - mid1

        l1 = num1[mid1 - 1] if mid1 > 0 else float('-inf')
        r1 = num1[mid1] if mid1 < n else float('inf')
        l2 = num2[mid2 - 1] if mid2 > 0 else float('-inf')
        r2 = num2[mid2] if mid2 < m else float('inf')

        if l1 <= r2 and l2 <= r1:
            if total % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2
            else:
                return min(r1, r2)
        elif l1 > r2:
            r = mid1 - 1
        else:
            l = mid1 + 1

        
print(findMedianSortedArrays([2,3,6,15,17],[1,3,4,7,10,12]))


        

