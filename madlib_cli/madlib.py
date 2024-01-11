def welcome():
    print('Welcome to MadLibs. You will be prompted here in the terminal. To play, type your answer and enter. Have fun!')

welcome()

def read_template (path):
    """ 
    takes in a path to a template file and returns the stripped text
    """

  #  return "It was a {Adjective} and {Adjective} {Noun}."  
    with open(path) as file:
        contents = file.read()
        return contents.strip()


def parse_template(template):
    # return "It was a {} and {} {}.", ("Adjective", "Adjective", "Noun")
    parts = []
    stripped = ""

    capturing = False
    capture = ""

    for char in template:
        if capturing:
            if char == "}":
                parts.append(capture)
                capture = ""
                capturing = False
                stripped += "{}"
            else:
                capture += char
        else:
            if char != "{":
                stripped += char

            if char == "{":
                capturing = True

    return stripped, tuple(parts) 


def merge(stripped_template, parts):
    """
    Given "It was a {} and {} {}." and ("dark", "stormy", "night") return "It was a dark and stormy night."
    """
    # return "It was a dark and stormy night."
    # * unpacks the tuple ie. turns into separate arguments - called star args or splat args
    return stripped_template.format(*parts)

if __name__== "__main__": 
    template = read_template('assets/dark_and_stormy_night_template.txt')
    # print(template)

    stripped_template, parts = parse_template(template)
    print(stripped_template)

    responses = []

    for part in parts:
        response = input(f"Please enter a {part}: ")
        responses.append(response)

    merged = merge(stripped_template, responses)

    print(merged)

    with open('assets/dark_and_stormy_night.txt', 'w+') as file:
        file.write(merged)
