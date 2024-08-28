from random import randint
import sqlite3

DATABASE_PATH = 'card.s3db'
CREATE_TABLE_SQL = """CREATE TABLE IF NOT EXISTS card (id INTEGER, number TEXT, 
pin TEXT, balance INTEGER DEFAULT 0); """
INSERT_DATA = """INSERT INTO card (id, number, pin, balance) VALUES (?, ?, ?, ?); """
CHECK_CARD = """SELECT * FROM card WHERE number = ?; """
CHECK_CREDENTIAL = """SELECT pin FROM card WHERE number = ?"""
DELETE_ACCOUNT = """DELETE FROM card WHERE number = ?"""
DEPOSIT = """UPDATE card SET balance = balance + ? WHERE number = ?"""


class BankDatabase:
    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_PATH)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(CREATE_TABLE_SQL)

    def create_account(self, id_, number, pin, balance):
        data_tuple = (id_, number, pin, balance)
        with self.connection:
            self.connection.execute(INSERT_DATA, data_tuple)

    def check_credential(self, number):
        with self.connection:
            return self.connection.execute(CHECK_CREDENTIAL, (number,)).fetchone()

    def check_card(self, card_number):
        with self.connection:
            result = self.connection.execute(CHECK_CARD, (card_number,)).fetchone()
            return result

    def delete_card(self, number):
        with self.connection:
            self.connection.execute(DELETE_ACCOUNT, (number,))

    def deposit(self, deposit_amount, number):
        data_tuple = (deposit_amount, number)
        with self.connection:
            self.connection.execute(DEPOSIT, data_tuple)

    def transaction(self, from_account, to_account, amount):
        try:
            with self.connection:
                self.connection.execute("BEGIN TRANSACTION")
                self.connection.execute("UPDATE card SET balance = balance - ? WHERE number = ?",
                                        (amount, from_account))
                self.connection.execute("UPDATE card SET balance = balance + ? WHERE number = ?",
                                        (amount, to_account))
                self.connection.execute("COMMIT")
                print("Transaction complete")
        except sqlite3.Error as error:
            self.connection.execute("ROLLBACK")
            print('Transfer failed!', error)

    def close(self):
        self.connection.close()


class BankSystem:
    def __init__(self):
        self.database = BankDatabase()
        self.menu()

    def generate_account(self):
        card_number = self.luhn_checked_num_generator()
        id_ = self.luhn_checked_num_generator()[6:-1]
        pin = str.zfill(str(randint(0000, 9999)), 4)
        self.database.create_account(id_, card_number, pin, balance=0)
        print(f'Your card has been created\nYour card number:\n{card_number}\nYour card PIN:\n{pin}')

    def login(self):
        try:
            card_input = input('Enter your card number: ')
            pin_input = input('Enter your PIN: ')

            if self.database.check_credential(card_input)[0] == pin_input:
                print('You have successfully logged in!')
                self.account_menu(card_input)
            else:
                print('Wrong card number or PIN!')
        except TypeError:
            print('Wrong card number or PIN!')

    def transfer(self, card):
        while True:
            print('Transfer')
            destination_account = input('Enter card number:\n')
            if not self.luhn_check(destination_account):
                print('Probably you made a mistake in the card number. Please try again!')
            elif not self.database.check_card(destination_account):
                print('Such a card does not exist.')
            elif destination_account == card:
                print("You can't transfer money to the same account!")

            else:
                amount = int(input('Enter how much money you want to transfer:\n'))
                if amount > self.database.check_card(card)[3]:
                    print('Not enough money!')
                    break
                self.database.transaction(card, destination_account, amount)
                break

    def deposit(self, card):
        income = int(input('Enter income:\n'))
        self.database.deposit(income, card)
        print('Income was added!')

    def exit_program(self):
        print('Bye!')
        self.database.close()
        quit()

    def account_menu(self, card):
        options = {
            '1': lambda: print(f'Balance: {self.database.check_card(card)[3]}'),
            '2': lambda: self.deposit(card),
            '3': lambda: self.transfer(card),
            '4': lambda: self.database.delete_card(card),
            '5': lambda: print('You have successfully logged out!'),
            '0': lambda: self.exit_program()
        }
        print('1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit')

        while True:
            choice = input()
            operation = options.get(choice)
            if operation:
                operation()
                if choice == '5':
                    return
            else:
                print('Invalid choice!')

    def menu(self):
        print('1. Create an account\n2. Log into account\n0. Exit')
        while True:
            choice = input()
            if choice == '0':
                print('Bye')
                self.database.close()
                quit()
            elif choice == '1':
                self.generate_account()
            elif choice == '2':
                self.login()

    @staticmethod
    def luhn_checked_num_generator():
        iin = '400000'
        random_card_number = str.zfill(str(randint(000000000, 999999999)), 9)
        account_number = iin + random_card_number
        card_check = [int(i) for i in account_number]

        for index, _ in enumerate(card_check):
            if index % 2 == 0:
                card_check[index] *= 2
            if card_check[index] > 9:
                card_check[index] -= 9

        check_sum = str((10 - sum(card_check) % 10) % 10)
        account_number += check_sum
        return account_number

    @staticmethod
    def luhn_check(card_number):
        card_digits = [int(digit) for digit in str(card_number)]
        card_digits.reverse()

        for i in range(1, len(card_digits), 2):
            card_digits[i] *= 2
            if card_digits[i] > 9:
                card_digits[i] -= 9

        total_sum = sum(card_digits)
        return total_sum % 10 == 0


if __name__ == '__main__':
    basuria_central_bank = BankSystem()

