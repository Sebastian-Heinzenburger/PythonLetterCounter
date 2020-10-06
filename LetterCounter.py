def main(string):
    [print_letter(l) for l in string if l not in already_counted]


def print_letter(letter):
    already_counted.append(letter)
    print(f'{letter}: {test_string.count(letter)}')


if __name__ == '__main__':

    already_counted = []
    test_input = input()

    test_string = test_input if test_input != '' else "Hello World!"
    main(test_string)
