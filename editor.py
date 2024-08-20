# write your code here
import formatters as formatter


def save_content(stored_text):
    with open('output.md', 'w') as file:
        for line in stored_text:
            file.write(line)


def main():
    formatters = {"plain": formatter.plain,
                  "bold": formatter.bold,
                  "italic": formatter.italic,
                  "header": formatter.header,
                  "link": formatter.link,
                  "inline-code": formatter.inline_code,
                  "new-line": formatter.newline,
                  "ordered-list": formatter.ordered_list,
                  "unordered-list": formatter.create_list}
    content = []

    while True:
            user_input = input('Choose a formatter: ').strip().lower()

            if user_input == '!done':
                save_content(content)
                break
            elif user_input == '!help':
                formatter.print_help_menu()
            elif user_input in formatters:
                content.append(formatters[user_input]())
                print(''.join(content))
            else:
                print('Unknown formatting type or command')


if __name__ == '__main__':
    main()
