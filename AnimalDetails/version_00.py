def get_animals_details(animal):
    result = None
    if animal:
        if "type" in animal:
            if "name" in animal:
                if "gender" in animal:
                    result = f"{animal['name']} is a {animal['gender']} {animal['type']}"
                else:
                    result = 'No animal gender'
            else:
                result = 'No animal name'
        else:
            result = 'No animal type'
    else:
        result = 'No animal'
    return result