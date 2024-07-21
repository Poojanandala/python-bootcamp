#find the maximum sub array sum
n=5
k=3
ans=0
arr=[9,2,5,3,7]
for i in range(n-k+1):
    sub_arr=arr[i:i+k]
    print("find thescore for sum sub",sub_arr)
    sum=0
    for ind in range(1,k+1):
        sum += sub_arr[ind-1]*ind
        print("sum is",sum)
    print("score:",sum)
    if sum>ans:
        ans=sum
    print(ans)

