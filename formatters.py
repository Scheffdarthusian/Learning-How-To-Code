def print_help_menu():
    print('Available formatters: plain bold italic header link inline-code new-line\nSpecial commands: !help !done')


def plain():
    return input("Text: ")


def bold():
    return f'**{input("Text: ")}**'


def italic():
    return f'*{input("Text: ")}*'


def header():
    while True:
        try:
            level = int(input('Level: '))
            if 1 <= level <= 6:
                return f'{"#" * level} {input("Text: ")}\n'
            else:
                print('The level should be within the range of 1 to 6')
        except ValueError:
            print('Please enter a number')


def link():
    while True:
        try:
            label = input('Label: ')
            url = input('URL: ')
        except ValueError:
            print('Please enter a URL')
        else:
            break
    return f'[{label}]({url})'


def inline_code():
    return f'`{input("Text: ")}`'


def newline():
    return '\n'


def create_list(ordered=False):
    result = ''
    while True:
        try:
            num_row = int(input('Number of rows: '))
            if num_row > 0:
                for num in range(1, num_row + 1):
                    text = input(f'Row #{num}: ')
                    if ordered:
                        result += f'{num}. {text}\n'
                    else:
                        result += f'* {text}\n'
                break
            else:
                print('Please enter a positive integer')
        except ValueError:
            print('Please enter a number')

    return result


def ordered_list():
    return create_list(ordered=True)
