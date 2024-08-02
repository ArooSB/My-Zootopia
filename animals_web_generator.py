import json

def load_data(file_path):
    """
    Load data from a JSON file.

    Parameters:
    ----------
    file_path : str
        The path to the JSON file containing animal data.

    Returns:
    -------
    list
        A list of dictionaries, each representing an animal with its details.
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """
    Serialize a single animal object into HTML format.

    Parameters:
    ----------
    animal_obj : dict
        A dictionary containing details about an animal.

    Returns:
    -------
    str
        An HTML string representing the animal's details in list item format.
    """
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal_obj["name"].upper()}</div>\n'

    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += (f'<div class="card__info"><strong>Diet:</strong> '
                   f'{animal_obj["characteristics"]["diet"]}</div>\n')

    if 'locations' in animal_obj and animal_obj['locations']:
        output += (f'<div class="card__info"><strong>Location:</strong> '
                   f'{", ".join(animal_obj["locations"])}</div>\n')

    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += (f'<div class="card__info"><strong>Type:</strong> '
                   f'{animal_obj["characteristics"]["type"]}</div>\n')

    if 'description' in animal_obj:
        output += f'<div class="card__text">{animal_obj["description"]}</div>\n'

    if 'average_lifespan' in animal_obj:
        output += (f'<div class="card__text"><strong>Average Lifespan:</strong> '
                   f'{animal_obj["average_lifespan"]} years</div>\n')

    if 'habitat' in animal_obj:
        output += f'<div class="card__text"><strong>Habitat:</strong> {animal_obj["habitat"]}</div>\n'

    output += '</li>\n'
    return output


def generate_html(data):
    """
    Generate HTML content based on animal data.

    Parameters:
    ----------
    data : list
        A list of dictionaries, each representing an animal's details.

    Returns:
    -------
    str
        An HTML string containing all animal details.
    """
    output = ''
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


def generate_full_html(template_path, animals_data):
    """
    Read the HTML template and replace placeholder with serialized animal data.

    Parameters:
    ----------
    template_path : str
        The path to the HTML template file.
    animals_data : list
        A list of dictionaries, each representing an animal's details.

    Returns:
    -------
    str
        A complete HTML string with the template and animal data merged.
    """
    with open(template_path, "r") as file:
        template = file.read()

    animal_details = generate_html(animals_data)
    html_content = template.replace('__REPLACE_ANIMALS_INFO__', animal_details)

    return html_content


def write_html(new_file_path, html_content):
    """
    Write the new HTML content to a new file.

    Parameters:
    ----------
    new_file_path : str
        The path to the new HTML file.
    html_content : str
        The new HTML content to write into the file.
    """
    with open(new_file_path, "w") as file:
        file.write(html_content)


def main():
    """
    Main function to load data, generate HTML, and write to a new file.
    """
    animals_data = load_data('animals_data.json')
    html_content = generate_full_html('animals_template.html', animals_data)
    write_html('zootopia.html', html_content)
    print("Zootopia is Ready")


if __name__ == "__main__":
    main()
