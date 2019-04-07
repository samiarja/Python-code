import time
start=time.time()
timecount = time.time() - start

a=[[1,1,4],[5,5,6],[7,9,9]]

def diagonal_sum(given_array):
    for i in range (len(given_array)):
        for j in range (len(given_array[i])):
            add_up = given_array[i][j] + given_array[i+1][j+1] +given_array[i+2][j+2]
            return add_up
  
print(diagonal_sum(a))

def rooks_are_safe(chessboard):
    n=len(chessboard)
    for row_i in range(n):
        row_count = 0
        for col_i in range(n):
            row_count += chessboard[row_i][col_i]
        if row_count > 1:
            return False
    for col_i in range(n):
        col_count = 0
        for row_i in range(n):
            col_count += chessboard[row_i][col_i]
        if col_count > 1:
            return False
        return True
print(rooks_are_safe([[0,0,0],[1,0,1],[0,0,0]]))
print(timecount)


age = {"Emily":20,"Sami":24}
if "Sami" in age:
    print("Found!..")
else:
    print("Not found!..")



    
