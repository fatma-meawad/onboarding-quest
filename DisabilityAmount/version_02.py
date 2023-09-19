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
    # Define the eligibility conditions
    eligibility = (
        seniority >= 2
        and months_disabled <= 12
        and not is_part_time
        and age >= 62
        and disability_percentage >= 60
        and income <= 40000
        and insurance_type == "disability"
    )

    # If eligible, calculate the benefit amount based on a formula
    if eligibility:
        benefit_amount = (income * disability_percentage) / 100
        return benefit_amount

    return 0
