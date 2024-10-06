def main(list_trees):
    res = 0
    list_trees = sorted(list_trees)
    bloomed = 0
    for i in range(len(list_trees)):
        if list_trees[i] <= bloomed:
            bloomed += 1
        else:
            res += list_trees[i]-bloomed
            bloomed += list_trees[i]-bloomed
    return res

assert main([0]) == 0, main([0])
assert main([0, 0, 3, 3]) == 1, main([0, 0, 3, 3])
assert main([10]) == 10, main([10])
assert main([5, 0, 3, 2, 1, 4]) == 0, main([5, 0, 3, 2, 1, 4])
assert main([0,0,0,0,11]) == 7, main([0,0,0,0,11])

