import json


def load_html_data(file_path_html):
  """ Loads a JSON file """
  with open(file_path_html, "r") as handle:
    html_data = handle.read()
    return html_data


def load_json_data(file_path_json):
  """ Loads a JSON file """
  with open(file_path_json, "r") as handle:
    json_data = json.load(handle)
    return json_data


def parse_json_data(json_data):
  output = ""
  for animal in json_data:
    output += f'\nName: {animal["name"]}\n'
    output += f'Diet: {animal["characteristics"]["diet"]}\n'

    if animal["locations"]:
      first_location = animal["locations"][0]
      output += f'Location: {first_location}\n'

    if "type" in animal["characteristics"]:
      output += f'{animal["characteristics"]["type"]}\n'
    else:
      output += f'Type not available.\n\n'
  return output


def replace_animals_info(html_template, animals_info):
    return html_template.replace('__REPLACE_ANIMALS_INFO__', animals_info)


def write_to_file(file_path, content):
  with open(file_path, "w") as handle:
    handle.write(content)


def main():
  json_data = load_json_data("animals_data.json")
  html_template = load_html_data("animals_template.html")
  animals_info = parse_json_data(json_data)
  new_html_content = replace_animals_info(html_template, animals_info)
  write_to_file("animals_template.html", new_html_content)


if __name__ == "__main__":
  main()