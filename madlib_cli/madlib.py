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

