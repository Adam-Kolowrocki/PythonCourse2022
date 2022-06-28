class Logger:
    def __init__(self):
        self.log = log

    def show_log(self):
        print(self.calue())


class Warning_Log():
    def value(self):
        return 'Ostrzeżenie !!!'


class Error_Log():
    def value(self):
        return 'Uwaga Błąd'


class Info_Log():
    def value(self):
        return 'Informacja z systemu'


def main():
    try:
        x = 4/0
    except ZeroDivisionError:
        error = Error_Log()
        log = Logger(error)
        log.show_log()


if __name__ == "__main__":
    main()