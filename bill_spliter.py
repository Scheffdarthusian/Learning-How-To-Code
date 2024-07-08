import random


def get_guest_list(num_of_guests):
    print('Enter the name of every friend (including you), each on a new line:')
    return {input().strip(): 0 for _ in range(num_of_guests)}


def get_user_choice(prompt):
    while True:
        response = input(prompt).strip().lower()
        if response in ['yes', 'no']:
            return response == 'yes'
        print('Please enter Yes or No:')


def get_positive_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            if value == 0:
                print('No one is joining for the party')
                return 0
            print('Please enter a positive number')
        except ValueError:
            print('Invalid input, Please enter a positive number:')


def bill_spliter(total, guests, lucky_one=None):
    payers = len(guests) - bool(lucky_one)
    share = round(total / payers, 2) if payers else 0
    return {guest: share if guest != lucky_one else 0 for guest in guests}


def main():
    num_of_guests = get_positive_number('Enter the number of friends joining (including you): ')
    if num_of_guests == 0:
        return

    guests = get_guest_list(num_of_guests)

    total = float(input('Enter the total bill value: '))
    if total <= 0:
        print('Bill cannot be zero or negative!')
        return

    lucky_one_feature = get_user_choice('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_one = random.choice(list(guests)) if lucky_one_feature else None

    if lucky_one:
        print(f'{lucky_one} is the lucky one!')
    else:
        print('No one is going to be lucky')

    split_bill = bill_spliter(total, guests, lucky_one)
    print(split_bill)


if __name__ == '__main__':
    main()
