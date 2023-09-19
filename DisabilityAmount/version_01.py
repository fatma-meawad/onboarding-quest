def disability_amount(
    seniority: int,
    months_disabled: int,
    is_part_time: bool,
    age: int,
    disability_percentage: int,
    income: int,
    insurance_type: str,
):
    """Calculates the amount of disability benefits that an individual is eligible for.
    Takes into account factors such as seniority, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type.
    """
    if (
        seniority < 2
        or months_disabled > 12
        or is_part_time
        or age < 62
        or disability_percentage < 60
        or income > 40000
        or insurance_type != "disability"
    ):
        return 0
    else:
        # If all conditions are met, calculate the benefit amount based on a formula
        benefit_amount = (income * disability_percentage) / 100
        return benefit_amount
