def min_max(arr,low,high):
    if(low==high):
        min=arr[low]
        max=arr[high]
    elif(low==high-1):
        if(arr[low] >= arr[high]):
            min=arr[high]
            max=arr[low]
        else:
            min=arr[low]
            max=arr[high]
    else:
        mid=(low+high)//2
        min,max=min_max(arr,low,mid)
        min1,max1=min_max(arr,mid+1,high)
        if(max1>max):
            max=max1
        if(min1<min):
            min=min1
    return min,max
arr=[7,2,9,3,1,6,7,8,4]
min,max=min_max(arr,0,len(arr)-1)
print(" Minimum : ",min)
print(" Maximum : ",max)