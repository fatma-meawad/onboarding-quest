def get_animals_details(animal):
    result = None

    if not animal:
        result = "No animal"
    elif not "type" in animal:
        result = "No animal type"
    elif not "name" in animal:
        result = "No animal name"
    elif not "gender" in animal:
        result = "No animal gender"
    else:
        result = f"{animal['name']} is a {animal['gender']} {animal['type']}"

    return result
