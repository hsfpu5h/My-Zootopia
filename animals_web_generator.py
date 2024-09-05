import os
import requests


def get_api_data(name):

    api_key = os.getenv('API_NINJAS_KEY')
    api_url = f"https://api.api-ninjas.com/v1/animals?name={name}"
    response = requests.get(api_url, headers={"X-Api-Key": api_key})
    if response.status_code == 200:
        try:
            data = response.json()
            if data:
                return data
        except Exception as error:
            print(f"Error: {error}")
    return None


def load_html_data(file_path_html):
    with open(file_path_html, "r") as handle:
        html_data = handle.read()
        return html_data


def serialize_animal(animal):
    output = ""
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += f'  <p class="card__text"><strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

    if animal["locations"]:
        output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    if "type" in animal["characteristics"] and animal["characteristics"]["type"]:
        output += f'{animal["characteristics"]["type"]}<br/>\n'
    else:
        output += 'Type not available.<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'
    return output


def parse_json_data(api_data):
    output = ""
    for animal_obj in api_data:
        output += serialize_animal(animal_obj)
    return output


def replace_animals_info(html_template, api_data):
    print("Website was successfully generated to the file animals.html.")
    return html_template.replace('__REPLACE_ANIMALS_INFO__', api_data)


def write_to_file(file_path, content):
    with open(file_path, "w") as handle:
        handle.write(content)


def main():
    name = input("What animal?: ")
    api_data = get_api_data(name)
    if api_data:
        html_template = load_html_data("animals_template.html")
        api_data_json = parse_json_data(api_data)
        api_html_content = replace_animals_info(html_template, api_data_json)
        write_to_file("animals.html", api_html_content)
    else:
        error_message_html = f"""
                <html>
                <head><title>Animal Not Found</title></head>
                <body>
                    <h2>The animal '{name}' doesn't exist.</h2>
                </body>
                </html>
                """
        write_to_file("animals.html", error_message_html)


if __name__ == "__main__":
    main()
