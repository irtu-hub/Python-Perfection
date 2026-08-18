from payroll.calculations import calculate_net_salary
from payroll import validation


basic_salary = 1200


if validation.is_valid_salary(basic_salary):

    net_salary = calculate_net_salary(
        basic_salary=basic_salary,
        allowance=200,
        deduction=50
    )

    print(f"Net Salary: {net_salary:.2f} OMR")

else:
    print("Invalid salary")