my_list=list(map(int,input().split(",")))
print(*my_list)
print("enter yor choice")
choice=int(input())
if(choice==1):
    my_list.append(5)
    print(*my_list)
elif(choice==2):
    my_list.pop()
    print(*my_list)
elif(choice==3):
    my_list.sort()
    print(*my_list)
