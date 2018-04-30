f = open('seven.txt','r')
f = f.readlines()
nums = []
i = 0
for idx, line in enumerate(f):
    if idx % 3 == 2:
        i += 1
    