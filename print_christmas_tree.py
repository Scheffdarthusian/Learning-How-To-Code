def create_postcard():
    postcard = [[' ' for _ in range(50)] for _ in range(30)]
    for i in range(50):
        postcard[0][i] = '-'
        postcard[29][i] = '-'
    for i in range(1, 29):
        postcard[i][0] = '|'
        postcard[i][49] = '|'
    merry_xmas = "Merry Xmas"
    start_pos = (50 - len(merry_xmas)) // 2
    for i, char in enumerate(merry_xmas):
        postcard[27][start_pos + i] = char
    return postcard

def print_postcard(postcard):
    for row in postcard:
        print(''.join(row))

def place_tree_on_postcard(postcard, height, interval, start_line, start_col):
    if interval <= 0:
        print("Interval must be greater than 0")
        return

    # Place the top of the tree
    if 0 <= start_line < 30 and 0 <= start_col < 50:
        postcard[start_line][start_col] = 'X'
    if 0 <= start_line + 1 < 30 and 0 <= start_col < 50:
        postcard[start_line + 1][start_col] = '^'

    # Body of the tree
    counter = 0  # Counter for positions marked with numbers
    for i in range(height - 1):
        line = start_line + 2 + i
        if line >= 30:
            break
        stars_and_decorations = ''
        for j in range(2 * i + 1):
            if counter % interval == 0 and j % 2 == 0:
                stars_and_decorations += 'O'
            else:
                stars_and_decorations += '*'
            if j % 2 == 0:
                counter += 1
        tree_line = '/' + stars_and_decorations + '\\'
        for k, char in enumerate(tree_line):
            col = start_col - (i + 1) + k
            if 0 <= col < 50:
                postcard[line][col] = char

    # Base of the tree
    base_line = start_line + height + 1
    if base_line < 30:
        if 0 <= start_col - 1 < 50 and 0 <= start_col + 1 < 50:
            postcard[base_line][start_col - 1] = '|'
            postcard[base_line][start_col + 1] = '|'

def main():
    inputs = list(map(int, input().split()))
    if len(inputs) == 2:
        height, interval = inputs
        print_christmas_tree(height, interval)
    elif len(inputs) % 4 == 0:
        postcard = create_postcard()
        for i in range(0, len(inputs), 4):
            height = inputs[i]
            interval = inputs[i + 1]
            start_line = inputs[i + 2]
            start_col = inputs[i + 3]
            place_tree_on_postcard(postcard, height, interval, start_line, start_col)
        print_postcard(postcard)
    else:
        print("Invalid input format")

def print_christmas_tree(height, interval):
    if interval <= 0:
        print("Interval must be greater than 0")
        return

    # Top of the tree
    print(' ' * (height - 1) + 'X')
    print(' ' * (height - 1) + '^')

    # Body of the tree
    counter = 0  # Counter for positions marked with numbers
    for i in range(height - 1):
        spaces = ' ' * (height - i - 2)
        stars_and_decorations = ''
        for j in range(2 * i + 1):
            if counter % interval == 0 and j % 2 == 0:
                stars_and_decorations += 'O'
            else:
                stars_and_decorations += '*'
            if j % 2 == 0:
                counter += 1
        print(spaces + '/' + stars_and_decorations + '\\')

    # Base of the tree
    print(' ' * (height - 2) + '| |')

# Example usage
main()
