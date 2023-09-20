def get_animals_details(animal):
    result = None
    if (
        not animal
        or not "type" in animal
        or "name" not in animal
        or "gender" not in animal
    ):
        error_message = "No animal"

        if not animal:
            return error_message
        if "type" not in animal:
            error_message += " type"
        if "name" not in animal:
            error_message += " name"
        if "gender" not in animal:
            error_message += " gender"

        return error_message
    else:
        result = result = f"{animal['name']} is a {animal['gender']} {animal['type']}"

    return result
