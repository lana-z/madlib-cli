import re

def parse_template(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    
    placeholders = re.findall(r'\{(.*?)\}', text)
    template = re.sub(r'\{.*?\}', '{}', text)
    return template, placeholders