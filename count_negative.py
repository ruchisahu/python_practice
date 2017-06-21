
#count number of negative numbers in array,each row and column is in accending sorted order.

#is the 2d array always square shaped?
#what about 0? not counted as 0 number

#solution:1check each element but it takes n2 time
#2 start with position a[0][n-1] top right corner

def count_neg(a):
    count=0
    row=0
    col=len(a)-1
    while col>=0 and row<len(a):
               if a[row][col]<0:
                   count+=(col +1)
                   row+=1
               else:
                   col=col-1
    return count   
                
    
    
    
print(count_neg([[-4,-3,-1,0],[-2,-2,1,2],[0,1,2,3],[0,2,3,4]]))   


print(count_neg([[-4,-3],[-2,-2]])) 
    
print(count_neg([[0]])) 
