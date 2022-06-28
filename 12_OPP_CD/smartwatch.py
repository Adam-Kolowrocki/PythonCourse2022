class Watch():
    def __init__(self, brand):
        print('Watch {brand}', '-> wear on hand')


class Phone():
    def __init__(self):
        print('Phone', '-> call with it')


    def call(self):
        print('Phone', '-> call with it')


class SmartWatch(Watch, Phone):
    def __init__(self):
        print('SmartWatch is practical')
        super().__init__()


sw = SmartWatch()
sw.__call()
p = Phone()
w = Watch('Casio')
