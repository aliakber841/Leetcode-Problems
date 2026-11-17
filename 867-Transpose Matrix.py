class Solution(object):
    def transpose(self, matrix):
        result=[]
        for i in range(len(matrix[0])):
            new_row=[]
            for j in range(len(matrix)):
                new_row.append(matrix[j][i])
            result.append(new_row)
        return result