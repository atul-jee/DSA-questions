# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# Leetcode Set matrix zeroes
def Set(matrix,row,col):
    for i in range(len(matrix[row])):
        matrix[row][i]=0
    for j in range(len(matrix)):
        matrix[j][col]=0
    

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        f = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]      
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    f[i][j]=True
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if f[i][j]:
                    Set(matrix,i,j)
        
        