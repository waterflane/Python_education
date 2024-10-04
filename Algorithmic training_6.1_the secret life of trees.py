def main(list_trees):
    ...

assert main([0]) == 1, main([0])
assert main([0, 0, 3, 3]) == 1, main([0, 0, 3, 3])
assert main([10]) == 10, main([10])
assert main([5, 0, 3, 2, 1, 4]) == 0, main([5, 0, 3, 2, 1, 4])
assert main([0,0,0,0,11]) == 7, main([0,0,0,0,11])

