class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        stack=[]
        length=len(set(arr))
        for i in set(arr):
            if arr.count(i) not in stack:
                stack.append(arr.count(i))
        if length==len(stack):
            return True
        else:
            return False
        