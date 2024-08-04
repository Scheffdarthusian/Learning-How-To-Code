def print_christmas_tree(height):
    print(' ' * (height - 1) + 'X')
    print(' ' * (height - 1) + '^')

    for i in range(height - 1):
        spaces = ' ' * (height - i - 2)
        stars = '*' * (i * 2 + 1)
        print(spaces + '/' + stars + '\\')
    print(' ' * (height - 2) + '| |')


print_christmas_tree(int(input()))
