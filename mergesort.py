def mergesort(arr,low,high):
    if(low>=high):
        return 
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)

def merge(arr,low,mid,high):
    temp=[]
    left=low
    right=mid+1
    while(left<=mid and (right)<=high):
        if(arr[left]<=arr[right]):
            temp.append(arr[left])
            left=left+1
        else:
            temp.append(arr[right])
            right=right+1
    while(left<=mid):
        temp.append(arr[left])
        left=left+1
    while(right<=high):
        temp.append(arr[right])
        right=right+1
    for i in range(len(temp)):
        arr[low + i] = temp[i]
arr=[8,3,2,9,7,1,5,4]
mergesort(arr,0,len(arr)-1)
print(arr)