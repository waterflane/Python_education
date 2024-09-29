def main(input_list):
    input_list = sorted(list(set(input_list)))
    if input_list[0] > 0 and input_list[-1] > 0:
        return input_list[0]*input_list[1]
    elif input_list[0] == 0 and input_list[-1] > 0:
        return input_list[0]*input_list[1]
    elif input_list[0] < 0 and input_list[-1] == 0:
        return input_list[0]*input_list[-1]
    elif input_list[0] < 0 and input_list[-1] < 0:
        return input_list[-1]*input_list[-2]
    elif input_list[0] < 0 and input_list[-1] > 0:
        return input_list[0]*input_list[-1]





assert main([1,2,3,4]) == 2, main([1,2,3,4])
assert main([1,2,3,-4]) == -12, main([1,2,3,-4])
assert main([-1,-2,-3]) == 2, main([-1,-2,-3])
assert main([-1,-2,0]) == 0, main([-1,-2,0])
assert main([-1,2,0]) == -2, main([-1,2,0])
assert main([1,2,0]) == 0, main([1,2,0])
assert main([1,2]) == 2, main([1,2])

