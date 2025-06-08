# i/p = n = 13
# o/p = [1,10,11,12,13,2,3,4,5,6,7,9]
 
class Solution:
    def DFS(self, num:int, limit:int, result:list[int]):
        if num>limit:
            return
        result.append(num)

        for next_digit in range(10):
            next_num= (num*10)+next_digit
            if next_num>limit:
                return 
            self.DFS(next_num, limit, result)

    def lexicographic(self, n:int)->list[int]:
        result=[]
        for i in range(1,10):
            self.DFS(i, n , result)

        return result
    
# T.C: O(N)
# S.C: O(N) 