per1 = 12
num = 0
while per1 <= 99:
    per2 = 12
    while per2 <= 99:
        if per1 % per2 == 0 and per1 != per2:
            num = num + 1
            print(per1, ':', per2)
        per2 = per2 + 1
        # print(per1, ' - ', per2)
    per1 = per1 + 1
    
    # print(per1)
print (num)
