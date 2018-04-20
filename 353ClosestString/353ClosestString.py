strs = []
with open("inFile", "r") as f:
    for line in f:
        strs.append(line.strip())
strs.pop(0)
def stringDiff(str1, str2):
    diff = 0
    for i in range(0,len(str1)):
        if str1[i] != str2[i]:
            diff += 1
    return diff

results = []
for i in range(0,len(strs)):
    results.append(0)
    for j in range(0,len(strs)):
        if i == j:
            pass
        else:
            results[i] += stringDiff(strs[i], strs[j])
print(strs[results.index(min(results))])