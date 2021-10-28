def make_repeater(n: int):
    """Closure that returns n * string"""
    def repeater(string: str) -> str:
        assert type(string) == str, "Just strings allowed"
        return n * string

    return repeater

def run():
    """Main code"""
    repeater_10 = make_repeater(10)
    print(repeater_10("Hola"))

if __name__ == '__main__':
    """Excecute the main code"""
    run()
