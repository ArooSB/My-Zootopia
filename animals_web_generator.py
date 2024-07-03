import json

# Function to load JSON data from a file
def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

# Function to generate a string with animal details
def generate_animal_details(animals_data):
    output = ''
    for animal in animals_data:
        output += "<li class='cards__item'>\n"
        if 'name' in animal:
            output += f"  <div class='card__title'>Name: {animal['name']}</div>\n"
        if 'characteristics' in animal and 'diet' in animal['characteristics']:
            output += f"  <div class='card__text'>Diet: {animal['characteristics']['diet']}</div>\n"
        if 'locations' in animal and animal['locations']:
            output += f"  <div class='card__text'>Location: {animal['locations'][0]}</div>\n"
        if 'characteristics' in animal and 'type' in animal['characteristics']:
            output += f"  <div class='card__text'>Type: {animal['characteristics']['type']}</div>\n"
        output += "</li>\n"
    return output

# Function to read the HTML template and replace placeholder with animal details
def generate_html(template_path, animals_data):
    with open(template_path, "r") as file:
        template = file.read()

    animal_details = generate_animal_details(animals_data)
    html_content = template.replace('__REPLACE_ANIMALS_INFO__', animal_details)

    return html_content

# Function to write the final HTML content to a file
def write_html(output_path, html_content):
    with open(output_path, "w") as file:
        file.write(html_content)

# Load the data
animals_data = load_data('animals_data.json')

# Generate the HTML content
html_content = generate_html('animals_template.html', animals_data)

# Write the new HTML content to a file
write_html('animals.html', html_content)

print("HTML file has been generated: animals.html")


#git remote add origin https://github.com/yourname/My-Zootopia.git
#git branch -M main
#git push -u origin main
