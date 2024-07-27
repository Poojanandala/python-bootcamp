#print the sum if the input is given as 123helloworld
vowels=['a','e','i','o','u']
cosonants="bcdfghjklmnpqrstvwxyz"
check="0123456789"
ans=0
i="hello 123world"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)
print(ans)