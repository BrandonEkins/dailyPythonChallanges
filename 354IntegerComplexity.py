num = 1234567
print num
i = 1
arr = []
class Divisor(object):
    num1 = 0
    num2 = 0
    total = 0
    
while i != num:
    if (num % i == 0):
        divisor = Divisor()
        divisor.num1 = i
        divisor.num2 = num/i
        divisor.total = divisor.num1 + divisor.num2
        arr.append(divisor)
    i += 1

print min(z.total for z in arr)
