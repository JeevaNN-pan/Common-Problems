def find_max(arr,n):
    max=arr[0]
    for i in range(1,n):
        if max<arr[i]:
            max=arr[i]
    return max
        
arr=[1,2,3,4,5,7,5,8,]
n=len(arr)
ans=find_max(arr,n)
print("max element is",ans)
        
    