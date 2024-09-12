def mid_element(arr):
    filterarr=[num for num in arr if num>=0]
    mid_val=(len(filterarr)-1)//2
    print(filterarr[mid_val])
    
arr=[1,2,-3,4,-5,6,7]
mid_element(arr)