def main(a_min, b_min):
    writer = min(a_min,b_min) // 10
    painter = max(a_min,b_min) // 20
    return min(writer,painter)

assert main(40,80) == 4; main(40,80)
assert main(61,0) == 0; main(61,0)
assert main(10,80) == 1; main(10,80)
assert main(24,10) == 1; main(24,10)