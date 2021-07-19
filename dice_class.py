
class Dice:
    def __init__(self, name, low, high, results) -> None:
        # pass
        self.name = name
        self.low = low
        self.high = high
        self.r_array = results
        self.results = []
        self.set_ammount(0)

    def set_ammount(self, ammount):
        self.ammount = ammount

    def clear_results(self):
        del self.results
        self.results = []


def main():
    pass

if __name__ in '__main__':
    main()