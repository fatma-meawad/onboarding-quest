def calculate_disability_benefit(seniority: int, months_disabled: int, is_part_time: bool, age: int, disability_percentage: int, income: int, insurance_type: str):

    if seniority < 2 or months_disabled > 12 or is_part_time or age < 62 or disability_percentage < 60 or income > 40000 or insurance_type != "disability":
        return 0
    
    benefit_amount = (income * disability_percentage) / 100
    return benefit_amount