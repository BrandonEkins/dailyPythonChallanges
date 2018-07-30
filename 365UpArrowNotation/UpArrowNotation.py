
try:
    f =  open('f.txt', 'r'):
    f = f.read().split(" ")
    n1 = f[0]
    arrows = len(f[1])
    n2 = f[2]
except:
    print("failed to open file")

