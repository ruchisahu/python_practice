#Problem:all characters in string is unique or not?can not use additional data structure

#Questions:what about null string ?what should it return?
 #In case of 1 character
 
 #Solution: 1.one solution is to compare every character but it will take n2 time.
 #2 sort by your most efficient sorting algorithm that take nlogn time and compare elemnts
 #3 create boolean list with size 256
 
def unique_char(str):
     if len(str)<0:
         return False
     elif len(str)==0 or len(str)==1:
         return True
     unique=[False]*256
     for i in str:
         if unique[ord(i)] is True:  #return an integer representing the Unicode code ord[a] return 97
             return False
         unique[ord(i)]=True
     return True

print(unique_char("abab"))

print(unique_char("abcd"))

print(unique_char(""))

print(unique_char("a"))     
