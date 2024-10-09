def is_prim(n:int)->bool:
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    for d in range(5, int(n**0.5), 6):
        if(n%d==0 or n%(d+2)==0):
            return False
    return True

line = input()
vec = line.split(" ")

for a in vec:
    try:
        a = int(a)
        if is_prim(a):
            print(a)
    except ValueError:
        print("NO")