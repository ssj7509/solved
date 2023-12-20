import math
count=0
for c in str(math.factorial(int(input())))[::-1]:
    if c!='0':
        break
    else:
        count+=1
print(count)