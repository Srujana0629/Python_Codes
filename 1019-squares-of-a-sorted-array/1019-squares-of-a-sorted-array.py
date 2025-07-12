class Solution:
    def sortedSquares(self, num: List[int]) -> List[int]:
        left=0
        right=len(num)-1
        result=[]
        while left <=right:
            if abs(num[left])>abs(num[right]):
                result.append(num[left]**2)
                left+=1
            else:
                result.append(num[right]**2)
                right-=1
        result.reverse()
        return result


        