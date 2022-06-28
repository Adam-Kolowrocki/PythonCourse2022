class Account:
    def __init__(self, username):
        self.username = username
        self.__account_number = 'PL11 3333 4444 1111 2222 6666'

    def show_num(self):
        print('Current account number', self.__account_number)


user = Account('mrlycz2323')
user.show_num()
user.account_number = 'PL44 4444 8888 9999 1111 3333'
user.show_num()