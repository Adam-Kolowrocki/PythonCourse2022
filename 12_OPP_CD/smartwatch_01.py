class UsefulStuff:
    def __init__(self, name):
        print(name, 'is used to make life easier!')


class Watch(UsefulStuff):
    def __init__(self, watch_name):
        print(watch_name, 'is small and convenient')
        super().__init__(watch_name)

    def check_time(self):
        print('TIME')


class Phone(UsefulStuff):
    def __init__(self, phone_name):
        print(phone_name, 'can make a call')
        super().__init__(phone_name)

    def call(self):
        print('Calling....')


class SmartWatch(Watch, Phone):
    def __init__(self):
        print('SmartWatch is practical')
        super().__init__('SmartWatch')


sw = SmartWatch()
print(SmartWatch.__mro__)
