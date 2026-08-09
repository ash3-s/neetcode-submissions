class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        mid = 0
        for i in range(len(matrix)):
            mid = (l+r)//2
            if target > matrix[mid][0]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        l, r = 0, len(matrix[mid])-1
        for i in range(len(matrix[mid])):
            m = (l+r)//2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True
        return False
