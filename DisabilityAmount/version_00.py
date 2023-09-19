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
    conditions = [
        seniority < 2,
        months_disabled > 12,
        is_part_time,
        age < 62,
        disability_percentage < 60,
        income > 40000,
        insurance_type != "disability"
    ]
    if any(conditions):
        return 0
    # If all conditions are met, calculate the benefit amount based on a formula
    benefit_amount = (income * disability_percentage) / 100
    return benefit_amount

