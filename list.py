def chec(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x
print(chec([10,20,20,30]))
#pehle ekk vacant list mano phir agar woh vacant meh nhi hai toh add karo otherwisw usko retuen karo