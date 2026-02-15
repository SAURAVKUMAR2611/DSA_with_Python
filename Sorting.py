def Selection_sort(arr):
    for i in  range(len(arr)):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

def Bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]         
    return arr  

def Insertion_sort(arr):
   if len(arr) <= 1:
        return arr
   for i in range(len(arr)):
       key=i
       while(key>0 and arr[key-1]>arr[key]):
           arr[key],arr[key-1]=arr[key-1],arr[key]
           key-=1
   return arr

#def Merge_sort(arr):  will take post learning the Recussion and Backtracking in python

        