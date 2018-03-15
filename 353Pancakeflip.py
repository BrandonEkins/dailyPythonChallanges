import collections
r = open("pancakes.txt",'r')
number = r.readline()
pancakes = r.readline().split(" ")
pancakes = [int(i) for i in pancakes]
print pancakes
flips = 0
sortIndex = len(pancakes) 
def flipPancakes(pc, index):#index of cake to put at sortIndex
    global sortIndex
    global flips
    if index != 0:
        pc = list(reversed(pc[:(index+1)])) + pc[(index+1):]
        flips += 1
        print pc
    pc = list(reversed(pc[:sortIndex])) + pc[sortIndex:]
    print pc
    flips += 1
    return pc

def checkOrder(pc):
    i = len(pc)-1
    while i > 0:
        if pc[i] >= pc [i - 1]:
            i -= 1
        else:
            return False
    return True

while sortIndex > 0:
    pancakes = flipPancakes(pancakes, pancakes.index(max(pancakes[:sortIndex])))
    if checkOrder(pancakes):
        sortIndex = -1
    sortIndex -= 1 
   
print flips

