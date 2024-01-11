

file = open('assets/dark_and_stormy_night_template.txt')
contents = file.read()

def parse_template(contents):
    placeholders = []
    text = file.read()
    for word in text.split():
        if word.startswith('{') and word.endswith('}'):
            placeholder = word[1:-1]
            if placeholder not in placeholders:
                placeholders.append(placeholder)
    return placeholders

parse_template(contents)