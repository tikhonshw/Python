lis = [5, 7, 233, 8, 301, -1, 93, -4]
frs_max = lis[0]
sec_max = 0


for i in lis:
    if i > frs_max:
        sec_max = frs_max
        frs_max = i
    elif i > sec_max:
        sec_max = i

print(sec_max)
