from parse_template import parse_template

def welcome():
    print('Welcome to MadLibs. You will be prompted in the terminal. Type your answer and enter. Have fun!')


def main():
    welcome()
    template, placeholders = parse_template('assets/dark_and_stormy_night_template.txt')
    user_inputs = [input(f"Enter a {placeholder}: ") for placeholder in placeholders]
    madlib = template.format(*user_inputs)
    print(madlib)
    write_to_file(madlib)

def write_to_file(madlib):
    with open('completed_madlib.txt', 'w') as file:
        file.write(madlib)

if __name__ == '__main__':
    main()