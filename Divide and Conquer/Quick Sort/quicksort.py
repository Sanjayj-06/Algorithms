def quicksort(arr,low,high):
    if(low<high):
        partition_index=partition(arr,low,high)
        quicksort(arr,low,partition_index)
        quicksort(arr,partition_index+1,high)
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while(arr[i]<=pivot and i<=high+1):
            i=i+1
        while(arr[j]>pivot and j>=low-1):
            j=j-1
        if(i<j):
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
arr=[4,6,2,5,7,9,1,3]
quicksort(arr,0,len(arr)-1)
print(arr)
 