import re

def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s




#ToDo my way of solution
def my_capitalize():
    s=input()
    n = s.split()
    neww=[]
    FUll_Name = " "

    if len(s)< 1000:
        for i in range(len(n)):
            val =n[i]
            print(val)
            change_letter=re.sub('\b[a-z0-9]+\b', r'', val[0]).upper()
            name=val.replace(val[0], change_letter)
            neww.append(name)

        print(neww)
        FUll_Name=" ".join(neww)
        print(FUll_Name)

    return FUll_Name





capitalize()