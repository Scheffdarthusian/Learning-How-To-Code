def print_christmas_tree(height, interval):
    if interval <= 0:
        print("Interval must be greater than 0")
        return

    # Top of the tree
    print(' ' * (height - 1) + 'X')
    print(' ' * (height - 1) + '^')

    # Body of the tree
    num_counter = 0  # Counter for positions marked with numbers
    for i in range(height - 1):
        spaces = ' ' * (height - i - 2)
        row = ''
        for j in range(i * 2 + 1):
            if (j + 1) % 2 == 0:
                if num_counter % interval == 0:
                    row += 'O'
                else:
                    row += '*'
                num_counter += 1
            else:
                row += '*'
        print(spaces + '/' + row + '\\')

    # Base of the tree
    print(' ' * (height - 2) + '| |')


# Example usage
ht, itl = map(int, input().split())
print_christmas_tree(ht, itl)
