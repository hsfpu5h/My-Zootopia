import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def parse_data(animals_data):
  for animal in animals_data:
    print(f"Name: {animal["name"]}")
    print(f"Diet: {animal["characteristics"]["diet"]}")
    print(f"animal["locations"][0])

    if "type" in animal["characteristics"]:
      print(animal["characteristics"]["type"])
    else:
      print("Type not available")

    print()


def main():
  animals_data = load_data('animals_data.json')
  print(animals_data)
  parse_data(animals_data)


if __name__ == "__main__":
  main()