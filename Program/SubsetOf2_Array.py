def disjoint_arrays(arr1,arr2):
 for i in range(0,len(arr1)):
    for j in range(0,len(arr2)):
     if(arr1[i] == arr2[j]):
      break
 if(j == len(arr2)):
   return 0
 return 1;

arr1 = [1,2,3,4,5]
arr2 = [3,4,5]
res = disjoint_arrays(arr1,arr2)
if(res == 1):
 print("Array 2 is a subset of array 1")
else:
 print("Array 2 is not a subset of array 1")


