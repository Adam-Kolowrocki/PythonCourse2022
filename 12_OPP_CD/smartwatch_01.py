class UsefullStuff:
    def __init__(self, name):
        print(name, 'is very useful')

class Watch(UsefullStuff):
    def __init__(self, brand):
        print(f'Watch {brand}', '-> wear on hand')
        super().__init__()

    def check_time(self):
        print('TIME')

class Phone(UsefullStuff):
    def __init__(self):
        print('Phone', '-> call with it')
        # super().__init__('-- phone --')

    def call(self):
        print('Calling....')

class SmartWatch(Watch, Phone):
    def __init__(self):
        print('SmartWatch is practical')
        super().__init__('SmartWatch')

sw = SmartWatch()
print(SmartWatch.__mro__)