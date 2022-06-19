# W kodzie BMI ufamy, że użytkownik podaje wartość w kilogramach
# lub w metrach i rzutujemy do float. Co jeśli użytkownik poda wartość 60 kg ?
# Zmodyfikuj kod z ostatnich zajęć tak, aby wykluczyć powyższy przypadek.

import bmi


def open_advice(filename):
    with open(f'{filename}.txt') as f:
        advice = f.read()

    return advice


def get_value(message, min_max):
    while True :
        try:
            value = float(input(message))
            minimum, maximum = min_max(minimum, maximum+1)

            if not (value in range(minimum, maximum+1)):
                raise ValueError(f'Wartość {value} jest nieprwidłowa...')
            
        except (TypeError, ValueError):
            print('Musisz podać wartość liczbową używając "." jako separatora')
        else:
            return value


def main():
    w = get_value('Podaj wagę w kg', (20, 200))
    h = get_value('Podaj wzrost [m]', (1.4, 2.5))

    result = bmi.calc_bmi(h, w)
    status = bmi.get_bmi_status(result)
    advice = open_advice(status)
    print(status.upper(), '***************')
    print(advice)

if __name__ == "__main__":
    main()