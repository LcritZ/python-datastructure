# encoding = utf-8
# hello add new line

# while True:
#     number = input()
#     bon = 0
#     if number > 10:
#         if number > 20:
#             if number > 40:
#                 if number > 60:
#                     if number>100:
#                         bon += (number-100)*0.01
#                         number = 100
#                     bon += (number - 60)*0.015
#                     number = 60
#                 bon += (number - 40)* 0.03
#                 number = 40
#             bon += (number-20)*0.05
#             number = 20
#         bon += (number-10)*0.1
#         number = 10
#
#     bon += number*0.2
#     print(bon)
#     if bon == 0:
#         break


while True:
    num = int(raw_input())
    benefitrange = [100,60,40,20,10,0]
    percent = [0.01,0.015,0.03,0.05,0.1,0.2]
    bonus = 0
    for index in range(0,6):
        if num > benefitrange[index]:
            print(num,"-",benefitrange[index]," * ",percent[index])
            bonus += (num - benefitrange[index])*percent[index]
            num = benefitrange[index]
    print("bonus:",bonus)






