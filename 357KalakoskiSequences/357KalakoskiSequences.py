
number = input("input number")
def flip(x):
    if x == 1:
        return 2
    else: 
        return 1

def KalakoskiSequence(x):
    kSequence = [1,2,2]
    kIterator = 2
    flipper = 1
    t = 3
    while t != (x):
        if kSequence[kIterator] == 1:
            kSequence.append(flipper)
            flipper = flip(flipper)
            t += 1
        else:
            kSequence.append(flipper)
            kSequence.append(flipper)
            flipper = flip(flipper)
            t += 2
        kIterator += 1
    return kSequence

ks = KalakoskiSequence(int(number))
print(str(ks.count(1))+':'+str(ks.count(2)))