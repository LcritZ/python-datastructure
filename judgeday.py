#import switch

from functools import reduce

year = input("year: \n")
month = input("month: \n")
day = input("day: \n")

daynum = 0

flag = False
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            flag = True
    else:
        flag = True

monlist = [31,28,31,30,31,30,31,31,30,31,30,31]

monlist.sort()

def getsum(x,y):
    return x + y

#print(monlist[0:1])

#daynum = reduce(getsum,monlist[0:month-1])
print("now:",daynum)

for i in range(0,month-1) :
    daynum += monlist[i]

#daynum -= monlist[month]
daynum += day

if flag:
    daynum += 1

print(daynum)
