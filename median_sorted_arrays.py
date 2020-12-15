
# There are two sorted arrays A and B of size m and n respectively. 
# Find the median of the two sorted arrays. 
# The overall run time complexity should be O(log (m+n)).

arr1=[1, 3, 4, 7, 7]
arr2=[2, 3, 6, 8]

n=len(arr1)+len(arr2)

def med(arr1,arr2):
    n=len(arr1)+len(arr2)
    below=int(n/2)
    count=[]
    for x in range(0,below):
        if arr1[x]>arr2[x]:
            count.append(arr1[x])
            count.append(arr2[x])
        else:
            count.append(arr2[x])
            count.append(arr1[x])  
    print(count[below+1]) 

med(arr1,arr2)