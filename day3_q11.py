my_list=list(map(int,input().split()))
maximum=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maximum):
        maximum=my_list[i]
print(maximum)
