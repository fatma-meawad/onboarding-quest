def get_animals_details(animal):
    if not animal:
        return 'No animal'

    required_keys = ['type', 'name', 'gender']
    missing_keys = []
    for key in required_keys:
        if key not in animal:
            missing_keys.append(key)

    if missing_keys:
        return f'No animal {", ".join(missing_keys)}'
    
    animal_type = animal.get('type')
    animal_name = animal.get('name')
    animal_gender = animal.get('gender')

    return f"{animal_name} is a {animal_gender} {animal_type}"