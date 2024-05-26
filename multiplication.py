def print_numbers_with_conditions():
    for i in range(1, 10):
        for j in range(1, 10):
            if j == 3:
                continue
            print(j, end=' ')
        print()
        if i == 7:
            break

print_numbers_with_conditions()
