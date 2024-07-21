my_list=list(map(int,input().split()))
minimum=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]<minimum):
        minimum=my_list[i]
print(minimum)
