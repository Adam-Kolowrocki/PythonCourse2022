class BmiCalc:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate(self):
        bmi = round(self.weight / self.height ** 2, 2)
        return bmi


def main():
    adam = BmiCalc(85, 1.85)
    print(adam.calculate())


if __name__ == "__main__":
    main()
