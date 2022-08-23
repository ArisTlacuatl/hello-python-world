"""
After becoming famous, the CodeBots decided to move into a new building together. 
Each of the rooms has a different cost, and some of them are free, but there's a rumour that 
all the free rooms are haunted! Since the CodeBots are quite superstitious, 
they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.


Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, 
your task is to return the total sum of all rooms that are suitable for the CodeBots 
(ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
solution(matrix) = 9.
"""


def solution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    cols_affected = []
    total = 0
    #print(rows,cols)
    for i in range(0,rows):
        for j in range (0,cols):
            #Print all the numbers in the matrix
            #print(matrix[i][j])
            #If element in zero:
            if (matrix[i][j] == 0): 
                cols_affected.append(j)  #Save the column where the zero is
            #If element is different to zero:
            if (matrix[i][j] != 0):
                #If element is in column affected:
                if j in cols_affected:
                    #Do nothing
                    pass
                else:
                    #Add the value of the element to the total
                    total += matrix[i][j]
    #print(cols_affected)
    #print(total)           
    return total