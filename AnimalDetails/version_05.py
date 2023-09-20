def get_animals_details(animal):

    result = valid_animal(animal)
    if result == True:
        return f"{animal['name']} is a {animal['gender']} {animal['type']}"
    else:
        return result

def valid_animal(animal):
    if not animal:
        return "No animal"
    if "name" not in animal:
        return "No animal name"
    if "gender" not in animal:
        return "No animal gender"
    if "type" not in animal:
        return "No animal type"
    return True