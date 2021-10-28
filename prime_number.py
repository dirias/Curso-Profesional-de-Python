def prime(num: int) -> bool:
    """Returns a boolean if the number is prime"""
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    print(divisors)
    return True if len(divisors) == 2 else False

def run():
    """Main code"""
    num = int(input('Inter a natural number: '))
    print(f'The {num} is prime.') if prime(num) else print(f'The {num} is not prime.')
if __name__ == '__main__':
    """Excecute the main code"""
    run()