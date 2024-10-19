

i = [1,2,3,4,5,6,7,8]

def sum_and_count():
    sum=1
    for v in i:
        sum = sum + v
    print(sum)
    count = len(i)
    print(count)
       
        
    return sum, count
print(type(sum_and_count()))

    
a = 10
b = 20 
    
a,b = b, a

print(a)
print(b)
     