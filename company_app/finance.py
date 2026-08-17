def calculate_tax(salary, tax) :
    return salary * (tax/100)


def calculate_total(salary, incentives, deductions) :
    return salary + incentives - deductions