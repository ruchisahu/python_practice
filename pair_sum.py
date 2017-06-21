#sum of pair
#what if there are multiple sum 
#what if no pair sum to 10
#what about null list
#could the given array has negative umbers


def pair(a):
    seen={}
    for item in a:
        if(10-item)in seen:
            print(str(10-item)+str(item))
            
        else:
            seen[item]=1
   # print("no pair")    
    return
                
                
print(pair([2,3,4,5,6,7,8]))   

print(pair([2,3,4,5]))   

print(pair([2,3,4,5,6,7,8])) 

print(pair([2,3,4,5,6,-7,-8]))           