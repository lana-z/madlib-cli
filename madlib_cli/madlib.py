def welcome():
    print('Welcome to MadLibs. You will be prompted in the terminal. Type your answer and enter. Have fun!')

welcome()


def read_template (path):
    """ 
    takes in a path to a template file and returns the stripped text
    """

  #  return "It was a {Adjective} and {Adjective} {Noun}."  
    with open(path) as file:
        contents = file.read()
        return contents.strip()


def parse_template():

    """
    Given "It was a {Adjective} and {Adjective} {Noun}." Return "It was a {} and {} {}." i.e. takes in a stripped template string and returns a string with language parts removed and a separate list of those language parts.
    """
    # return "It was a {} and {} {}.", ("Adjective", "Adjective", "Noun")

    """
     It was a {Adjective} and {Adjective} {Noun}.
              ^capture mode
     It was a { 
     
     capture Adjective and keep going along string
     ["Adjective", "Adjective", "Noun"] - list
     ("Adjective," "Adjective," "Noun") - tuple
    """


    parts = []
    capture = ""
    for word in .split():
        if word.startswith("{"):
            parts.append(word.strip(".,?!"))
            capture += "{} "
        else:
            capture += word + " "
    return capture.strip(), tuple(parts) 


def merge(stripped_template, parts):
    """
    Given "It was a {} and {} {}." and ("dark", "stormy", "night") return "It was a dark and stormy night."
    """
    # return "It was a dark and stormy night."
    # * unpacks the tuple ie. turns into separate arguments - called star args or splat args
    return stripped_template.format(*parts)


# def main():
#     welcome()
#     template, placeholders = parse_template('assets/dark_and_stormy_night_template.txt')
#     user_inputs = [input(f"Enter a {placeholder}: ") for placeholder in placeholders]
#     madlib = template.format(*user_inputs)
#     print(madlib)
#     write_to_file(madlib)

# def write_to_file(madlib):
#     with open('completed_madlib.txt', 'w') as file:
#         file.write(madlib)

# if __name__ == '__main__':
#     main()