def Update(aib, a):
    while(a<=200000):
        aib[a]+=1
        a+=a&(-a)

def Query(aib, a):
    sum = 0
    while(a>0):
        sum+=aib[a]
        a-=a&(-a)
    return sum

sir = str(input()) # a sequence of caracters is given
vec = sir.split(" ") # splits the sequence into words
sol = nr = 0
aib = [] # binary indexed tree

for i in range(200001): # constructs the aib vector
    aib.append(0)

for i in vec:
    try:
        a = int(i)

        Update(aib, a) # add a to the binary indexed tree
        nr += 1

        sol+=nr-Query(aib, a) # how manny numbers with higher values that the actual variable are located before it
    except ValueError: # the code ignores the strings in the sequence
        sol+=0

print(sol)
