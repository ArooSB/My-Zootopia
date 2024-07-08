import json

# loading data from json file
def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

# Serialising a single animal object into HTML format
def serialize_animal(animal_obj):
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"].upper()}</div>\n'

    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f'<div class="card__info"><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</div>\n'

    if 'locations' in animal_obj and animal_obj['locations']:
        output += f'<div class="card__info"><strong>Location:</strong> {", ".join(animal_obj["locations"])}</div>\n'

    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f'<div class="card__info"><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</div>\n'

    if 'description' in animal_obj:
        output += f'<div class="card__text">{animal_obj["description"]}</div>\n'

    if 'average_lifespan' in animal_obj:
        output += f'<div class="card__text"><strong>Average Lifespan:</strong> {animal_obj["average_lifespan"]} years</div>\n'

    if 'habitat' in animal_obj:
        output += f'<div class="card__text"><strong>Habitat:</strong> {animal_obj["habitat"]}</div>\n'

    output += '</li>\n'
    return output

# Generate HTML content based on animal data
def generate_html(data):
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output

# Read the HTML template and replace placeholder with animal data extracted from json
def generate_full_html(template_path, animals_data):
    with open(template_path, "r") as file:
        template = file.read()

    animal_details = generate_html(animals_data)
    html_content = template.replace('__REPLACE_ANIMALS_INFO__', animal_details)

    return html_content

# Overwrite the HTML template with the updated data
def overwrite_html(template_path, html_content):
    with open(template_path, "w") as file:
        file.write(html_content)

# Load the data from animals_data.json
animals_data = load_data('animals_data.json')

# Generate the HTML data
html_content = generate_full_html('animals_template.html', animals_data)

# Overwrite the template with the updated data
overwrite_html('animals_template.html', html_content)

print("Zootopia is Ready")


#git remote add origin https://github.com/yourname/My-Zootopia.git
#git branch -M main
#git push -u origin main
