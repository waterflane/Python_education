a = int(input())
res = 0
for i in range(0, a):
    if i < 2:
        res = res+10.5
    else:
        res = res+4
print(res)