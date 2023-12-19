# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestNodes(self, root, queries):
        tree = []
        answer = []
        
        # make tree list
        def inorder(curr):
            if curr == None:
                return
            inorder(curr.left)
            tree.append(curr.val)
            inorder(curr.right)

        inorder(root)

        # find max, min
        for target in queries:
            N = len(tree)
            low, high = 0, N-1

            arr = [-1, -1]

            # exceptions
            if tree[low] >= target:
                arr[0] = -1 if tree[low] > target else tree[low]
                arr[1] = tree[low]
                answer.append(arr)
                continue
            
            if tree[high] <= target:
                arr[0] = tree[high]
                arr[1] = -1 if tree[high] < target else tree[high]
                answer.append(arr)
                continue
            
            # do binary search
            while low+1 < high:
                mid = (low+high)//2
                if target > tree[mid]: # false
                    low = mid
                else: # true
                    high = mid
                        
            # if same,
            if tree[high] == target:
                arr[0] = tree[high]
                arr[1] = tree[high]
                answer.append(arr)
                continue
            
            if tree[low] <= target:
                arr[0] = tree[low]

            if tree[high] > target:
                arr[1] = tree[high]

            answer.append(arr)
        
        return answer