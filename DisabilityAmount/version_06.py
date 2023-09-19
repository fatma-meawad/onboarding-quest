def disability_amount(
    years_at_company: int,
    months_on_disability: int,
    is_working_part_time: bool,
    age: int,
    disability_percentage: int,
    income: int,
    insurance_type: str,
):
    """Calculates the amount of disability benefits that an individual is eligible for.
    Takes into account factors such as years at company, months disabled, whether the individual
    is working part-time, age, disability percentage, income, and insurance type.

    Args:
        yearsAtCompany: The number of years the individual has been with the company.
        monthsOnDisability: The number of months the individual has been on disability.
        isWorkingPartTime: Whether the individual is working part-time.
        age: The individual's age.
        disabilityPercentage: The individual's disability percentage.
        income: The individual's income.
        insuranceType: The type of insurance the individual has.

    Returns:
        The amount of disability benefits the individual is eligible for.
    """

    if years_at_company < 2:
        raise ValueError("Must have at least 2 years of service")
    if months_on_disability > 12:
        raise ValueError("Cannot be on disability for more than 12 months")
    if is_working_part_time:
        raise ValueError("Part-time employees are not eligible for disability benefits")
    if age < 62:
        raise ValueError("Must be at least 62 years old")
    if disability_percentage < 60:
        raise ValueError("Disability percentage must be at least 60%")
    if income > 40000:
        raise ValueError("Income must be less than $40,000")
    if insurance_type != "disability":
        raise ValueError("Must have disability insurance")

    # If all conditions are met, calculate the benefit amount based on a formula
    benefit_amount = (income * disability_percentage) / 100
    return benefit_amount
