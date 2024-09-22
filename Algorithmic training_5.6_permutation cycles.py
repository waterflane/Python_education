def main(list2):
    res = 0
    used_id = []
    current_cyclу = []
    current_id = 0

    for i in range(len(list2)):
        if len(used_id) != len(list2):
            if bool(used_id) == False:
                used_id.append(0)
            else:
                cycly_off = False
                for iii in range(len(used_id)):
                    if iii != used_id[iii]:
                        current_id = i
                        cycly_off = True
                        break
                if cycly_off == False:
                    current_id = used_id[-1]+1
            for ii in range(len(list2)):
                current_id = list2[current_id]-1
                if current_id not in current_cyclу:
                    used_id.append(current_id)
                    current_cyclу.append(current_id)
                    used_id = list(set(used_id))
                    used_id.sort()
                else:
                    res+=1
                    current_cyclу = []
                    break
        else:
            break
    if res == 0:
        return 1
    return res


inp = list(map(int, input().split()))
print(main(inp))