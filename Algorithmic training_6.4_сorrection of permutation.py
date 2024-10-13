def main(len_s, s):
    s1 = set(range(1, len_s+1)) - set(s)
    s2 = []
    res = 0
    for i in range(len_s):
        if s[i] in s2 or s[i] >= len_s:
            s[i] = s1.pop()
            res += 1
        
        s2.append(s[i])
    return res, s

print(main(4, [1,100,3,3]))