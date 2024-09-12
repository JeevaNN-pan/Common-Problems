def find_max(arr,n):
    max=arr[0]
    sec=-1
    for i in range(1,n):
        if max<arr[i]:
            max=arr[i]
    for i in range(1,n):
        if arr[i]>sec and arr[i]!=max:
            sec=arr[i]
    return sec
        
arr=[1,2,3,4,5,7,5,8,9,14,15,16,17]
n=len(arr)
ans=find_max(arr,n)
print("sec largest element is",ans)
        
    