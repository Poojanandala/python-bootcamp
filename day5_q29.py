#write a program to count number of consonants in a string
vowel=['a','e','i','o','u']
consonant="bcdfghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
    if(i in consonant):
      c+=1
print(count)
print(c)