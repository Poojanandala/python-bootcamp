class Father:
    def father():
        return"father class"
class Mother:
    def mother():
        return"mother class"
class Kid(Father,Mother):
    def kid():
        return "iam kid who inherited my father and mother properties"
obj1=Kid
print(obj1.mother())
print(obj1.father())
print(obj1.kid())
