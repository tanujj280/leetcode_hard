 
# def rightSideView(root):
#     if not root:
#         return []
#     arr=[root.val]
#     def f(i,l):
#         while i:
#             print(i.val,"op")
#             if i.right:
#                 arr.append(i.right.val)
#                 i=i.right
#             elif i.left:
#                 arr.append(i.left.val)
#                 i=i.left
#             else:
#                 break
#             l+=1
#         return l
#     i=root
#     l=0
#     x=0
#     while i:
#         print(i.val,x,l)
#         while l==x:
#             x=f(i,l)
#             print(x,arr)
#             if not i:
#                 break
#             i=i.left
#             l+=1
#         if not i:
#             break
#         if i.right:
#             i=i.right
#         elif i.left:
#             i=i.left
#         else:
#             break
#         l+=1
#     return arr

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
root=TreeNode(-10)
b=TreeNode(20)
c=TreeNode(5)
c.right=TreeNode(2)
b.right=c
b.left=TreeNode(15)
root.right=b
root.left=TreeNode(9)

def maxPathSum(root) -> int:
        maxi=float("-inf")

        def f(i):
            nonlocal maxi
            if not i :
                return 0
            else:
                
                left=max(0,f(i.left))
                right=max(0,f(i.right))
                maxi=max(maxi,i.val+f(i.left)+f(i.right))
                return i.val+max(left,right)
        w=f(root)
        return maxi
print(maxPathSum(root))