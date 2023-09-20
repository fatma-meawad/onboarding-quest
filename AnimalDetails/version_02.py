def get_animal_details(animal):
    if not animal:
        return 'No animal'

    if "type" not in animal:
        return 'No animal type'
    if "name" not in animal:
        return 'No animal name'
    if "gender" not in animal:
        return 'No animal gender'

    return f"{animal['name']} is a {animal['gender']} {animal['type']}"