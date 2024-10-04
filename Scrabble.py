slovo = str(input())
slovo = slovo.upper()
res = 0

slovar = {
    ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'):1,
    ('D', 'G'):2,
    ('B', 'C', 'M', 'P'):3,
    ('F', 'H', 'V', 'W', 'Y'):4,
    ('K'):5,
    ('J', 'X'):6,
    ('Q', 'Z'):7}

for i in range(len(slovo)):
    for keys, items in slovar.items():
        if slovo[i] in keys:
            res += items
print(res)
