#this function takes in the file name and then seperates it into a list of each number represented as a string of its parts
def readNumbers(fileName):
    f = open(fileName,'r')
    f = f.readlines()
    nums = ["" for i in range(9)] 
    i = 0
    for line in f:
        for idx, c in enumerate(line[:-1]):
            nums[i] +=c
            if idx % 3 == 2:
                i = i + 1
        i = 0
    return nums                  

nums = readNumbers("seven.txt")
#these are the strings in same format output by the readNumbers function in order by number
numStrings = [' _ | ||_|','     |  |', ' _  _||_ ', ' _  _| _|', '   |_|  |', ' _ |_  _|', ' _ |_ |_|', ' _   |  |', ' _ |_||_|', ' _|_| _|']
finalNum = ""
for num in nums:
   finalNum += str(numStrings.index(num)) 
print(finalNum)
