def make_devision(n: float):
    """
        This closure returns a function that returns the devision of an x number by n
    """
    def division(x: float) -> float:
        return x / n
    return division

def run():
    n = float(input('Insert n: '))
    devision_n = make_devision(n)
    x = float(input('Insert x: '))
    print(devision_n(x))

if __name__ == '__main__':
    run()
