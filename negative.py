def negative_sum(a,b,c,d):
    nums=[a,b,c,d]
    neg=0
    for num in nums:
        if num<0:
            neg+=num
    print(neg)

a=-3
b=7
c=-1
d=4
negative_sum(a,b,c,d)    

            
    
    