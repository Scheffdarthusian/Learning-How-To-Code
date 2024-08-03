def print_christmas_tree(height):
    # Calculate the width of the tree based on the height
    width = 2 * height - 1
    # Create a list to store the rows of the tree
    tree = []

    # Add the top 'X' and '^'
    tree.append(' ' * ((width - 1) // 2) + 'X' + ' ' * ((width - 1) // 2))
    tree.append(' ' * ((width - 1) // 2) + '^' + ' ' * ((width - 1) // 2))

    # Add the tree body
    for i in range(height - 1):
        spaces = ' ' * (height - i - 2)
        stars = '*' * (2 * i + 1)
        row = spaces + '/' + stars + '\\' + spaces
        tree.append(row)

    # Add the stem
    stem_spaces = ' ' * ((width - 3) // 2)
    tree.append(stem_spaces + '| |' + stem_spaces)

    for row in tree:
        print(row)

print_christmas_tree(int(input()))
