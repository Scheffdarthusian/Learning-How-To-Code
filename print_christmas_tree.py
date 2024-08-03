def print_christmas_tree(height):
    #Calculate the width of the tree based on the height#
    width = 2 * height
    #Create a list to store the rows of the tree#
    tree = []

    #Add the top 'X' and '^'
    tree.append(' ' * (width // 2) + 'X' + ' ' * (width // 2))
    tree.append(' ' * (width // 2) + '^' + ' ' * (width // 2))

    #Add the tree body
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        row = spaces + '/' + stars + '\\' + spaces
        tree.append(row)
    #Add the stem
    stem_spaces = ' ' * (width // 2 - 1)
    tree.append(stem_spaces + '| |' + stem_spaces)

    for row in tree:
        print(row)


print_christmas_tree(int(input()))
