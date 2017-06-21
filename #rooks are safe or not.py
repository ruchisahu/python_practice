#rooks are safe or not chessboard or can rook attack one another.
#what the size of chessboard? any size
#is it always square shaped? yes
#could the given array be empty? no,atleast 1x1
#solution:if same column or same row then none of them will be able to attack each other

def rook_safe(chessboard):
     
    n=len(chessboard)
    for row in range(n):
	     row_count=0
	     for column in range(n):
		      row_count+=chessboard[row][column]
	     if row_count>1:
		      return False
			

    for column in range(n):
                
        col_count=0
        for row in range(n):
            col_count+=chessboard[row][column]
        if col_count>1:
            return False
			

    return True

print(rook_safe([[1,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,1,0]]))

print(rook_safe([[1,0,0,0],[1,0,0,1],[0,1,0,0],[0,0,1,0]]))

print(rook_safe([[1,0],[0,1]]))
print(rook_safe([[1,1],[1,1]]))

print(rook_safe([[1]]))

