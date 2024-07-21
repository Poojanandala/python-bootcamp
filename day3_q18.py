#find sum of even numbers in a given number
n=2341
sum=0
while n>0:
    r=n%10
    sum=sum/2+r
    n=n//10
print(sum)
