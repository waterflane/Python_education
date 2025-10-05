def dp(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    matrix = [[0 for x in range(l2)] for y in range(l1)]
    
    max_substring = 0
    str_max_substring = ''

    for y in range(l1):
        for x in range(l2):
            if str2[x] == str1[y]:
                if (x != 0 and x != len(str2) and y != 0) and matrix[y-1][x-1] != 0:
                    if max_substring < matrix[y-1][x-1]+1:
                        max_substring = matrix[y-1][x-1]+1
                        str_max_substring = str1[y-matrix[y-1][x-1]:y+1]
                    matrix[y][x] = matrix[y-1][x-1]+1
                else:
                    if max_substring < 1:
                        max_substring = 1
                        str_max_substring = str2[x]
                    matrix[y][x] = 1

    print(matrix)
    return max_substring, str_max_substring

print(dp('hish', 'fish'))
