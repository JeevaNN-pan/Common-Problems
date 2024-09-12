def find_div(a,d,q,r):
    div=d*q+r
    if div in a:
        return a.index(div)
    
a=[15,10,30]
d=5
q=2
r=5
print(find_div(a,d,q,r))
        
        
        