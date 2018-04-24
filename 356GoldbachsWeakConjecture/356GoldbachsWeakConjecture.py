
#Checks if the number is prime
def isPrime(pNum):
    for digit in range(pNum):
        if digit != 0 and digit != 1:
            if pNum % digit == 0:
                return False
	else:
	    return False
    return True

#Creates a list of all prime numbers that are less then the given number
def createPrimeList(oddnum):
    primeList = []
    for gnum in range(oddnum):
        if isPrime(gnum):
            primeList.append(gnum)
    return primeList

oddnum = 17 
primeList = createPrimeList(oddnum)
possibleFactors = []
for i in primeList:
    for j in primeList:
	for k in primeList:
	    if i + j + k == oddnum:
		possibleFactors.append([i,j,k])
lowestNum = oddnum
lowestFactors = []
for factors in possibleFactors:
	print sum(factors)
    #if sum(factors) < lowestNum:
	#lowestFactors = factors
	#lowestNum = sum(factors)	
print(lowestFactors)
