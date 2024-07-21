#find the elements that is present in k+ith index 
#k is given by user 
my_list=list(map(int,input().split(" ")))
k=int(input())
n=int(input())
if(len<k+n):
   print("error")
else:
    for  i in range(0,len(my_list)):
        print(my_list[k+n],end=" ")
        break
   
 

