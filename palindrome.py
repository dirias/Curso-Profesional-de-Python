def palidrome(string: str) -> bool:
    """Returns if the a word is a palinfrome or not"""
    return string == string[::-1]

def run():
    """Main code"""
    word = str(input('Insert a word or phrase: '))
    #Ternary if
    print(f'The word {word} is palindrome') if palidrome(word.lower()) else print(f'The word {word} is not a palindrome')

if __name__ == '__main__':
    """Excecute the main code"""
    run()