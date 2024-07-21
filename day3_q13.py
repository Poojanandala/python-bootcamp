my_list=list(map(int,input().split()))
maximum=my_list[0]
minimum=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maximum):
        maximum=my_list[i]
    elif(my_list[i]<minimum):
        minimum=my_list[i]
avg=(minimum+maximum)//2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)
