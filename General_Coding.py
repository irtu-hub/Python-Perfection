#print("Hello, Enterprise Python!")
# Name = "Irteza"
# Country = "Oman"
# Experience = 1.5
# print(Name)
# print(Country)
# print(Experience)
# print(type(Name))


# salary = int(input("Your Monthly salary please: ")) 
# annual_salary = salary * 12 
# print(annual_salary)
# from decimal import Decimal
# salary = Decimal('1250.75')
# allowance = Decimal('250.25')
# deduction = Decimal('125.10')
# net_salary = salary + allowance - deduction
# print(net_salary)
# employee_name = "   irteza saheem   "
# print(employee_name.strip().title())
# invoice_number = "INV-2026-00125"
# slice_invoice_number = invoice_number[4:8]
# print(slice_invoice_number) 
# question = "   What is the pending salary for employee 125?   "
# print(question.strip().lower())
# from decimal import Decimal


# name = "Irteza"
# department = "IT"
# salary = Decimal('350.00')
# annual_salary = salary * 12

# print(f"""
# Employee Name: {name}
# Department: {department}
# Salary: {salary}
# Annual Salary: {annual_salary:,}
# """)
# employees = ["Ahmed", "Sara", "Irteza", "John"]

# for employee in employees:
#     print(f"Processing {employee}")
# salaries = [450, 800, 1200, 2500, 600]
# for salary in salaries:
#     if(salary >= 1000):
#         print(salary)
# employees = [
#     {"name": "Ahmed", "department": "HR"},
#     {"name": "Sara", "department": "Finance"},
#     {"name": "Irteza", "department": "IT"}
# ]

# for employee in employees:
#     print(f"{employee['name']} works in the {employee['department']} department.")
# attempts = 0

# while attempts <3:
#     attempts += 1
#     print(f"Attempt {attempts}")

# employee_name = ""

# is_valid = employee_name.strip() != ""

# while not is_valid:
#     employee_name = input("Please enter your name: ")
#     is_valid = employee_name.strip() != ""

# balance = 1000
# payment = 250

# while balance > 0:
#     balance -= payment
#     print(f"Payment of {payment} processed. Remaining balance: {balance}")
# employees = ["Ahmed", "Sara", "Irteza", "John"]
# for employee in employees:
#     if employee == "Irteza":
#         print(f"Found {employee}")
#         break
# employees = [
#     {"name": "Ahmed", "active": True},
#     {"name": "Sara", "active": False},
#     {"name": "Irteza", "active": True},
#     {"name": "John", "active": False}
# ]


# for employee in employees:
#     if not employee["active"]:
#         continue
#     print(f"Processing active employee: {employee['name']}")
# transactions = [500, 1200, 800, 7000, 300, 900]
# for transaction in transactions:
#     if transaction > 5000:
#         print("Large transaction detected")
#         break
#     else:
#         print(f"processing {transaction}")
    
# employees = ["Ahmed", "Sara", "Irteza"]

# employees.append("John")
# employees.remove("Sara")
# employees[0] = "Ali"
# print(len(employees))
# sales = [1200, 1500, 1800, 2100, 2500]
# print(sales[0])
# print(sales[4])
# print(sales[0:3])
# print(sales[-2:])

# employee = ("Irteza", "IT", 350)
# name, dept, salary = employee
# print(name, dept, salary)
# print(len(employee))

# employee = {
#     "name": "Irteza",
#     "department": "IT",
#     "salary": 350
# }

# employee["salary"] += 500
# employee["status"] = "Active"
# employee.pop("department")
# nationality = employee.get("nationality", "")
# for key,value in employee.items():
#     print(f"{key}:{value}")


# employee = {
#     "name": "Ahmed",
#     "salary": 1200,
#     "allowance": 250,
#     "deduction": 100,
#     "status": "Active"
# }

# if employee["status"] == "Active":
#     salary,allowance,deduction = employee.get("salary",0), employee.get("allowance", 0), employee.get("deduction",0) 
#     print(salary)
#     net_salary = salary + allowance - deduction
#     employee["net_salary"] = net_salary
#     employee.pop("deduction") 
#     for key,value in employee.items():
#         print(f"{key}:{value}")   

# employees = [
#     {
#         "id": 101,
#         "name": "Ahmed",
#         "salary": 1200,
#         "allowance": 200,
#         "deduction": 100,
#         "status": "Active"
#     },
#     {
#         "id": 102,
#         "name": "Sara",
#         "salary": 1800,
#         "allowance": 300,
#         "status": "Active"
#     },
#     {
#         "id": 103,
#         "name": "John",
#         "salary": 1500,
#         "allowance": 150,
#         "deduction": 50,
#         "status": "Inactive"
#     }
# ]
# total_employees = 0
# processed_employees = 0
# skipped_employees = 0
# total_payroll = 0
# for emp in employees:
#     total_employees += 1
#     if emp["status"] == "Inactive":
#         skipped_employees += 1
#         continue
#     else:
#         processed_employees += 1
#         salary,allowance,deduction = emp.get("salary",0), emp.get("allowance", 0), emp.get("deduction",0)
            
#         net_salary = salary + allowance - deduction
#         emp["net_salary"] = net_salary
#         print(f"{emp["name"]} -> Net Salary: {net_salary}")
#         total_payroll += net_salary

# print(f"""
# ===============
# PAYROLL SUMMARY
# ===============
# Total employees: {total_employees}
# Processed employees: {processed_employees}
# Skipped employees: {skipped_employees}
# Total payroll: {total_payroll}

# """)

# departments = [
#     "HR",
#     "IT",
#     "Finance",
#     "HR",
#     "IT",
#     "Sales",
#     "Finance"
# ]
# dept_set = set(departments)
# print(len(dept_set))
  
# employee_ids = [
#     101, 102, 103, 104,
#     102, 105, 101, 106
# ]

# duplicate_ids = employee_ids.copy()
# print(duplicate_ids)
# unique_employee_ids = set(employee_ids)

# if len(unique_employee_ids) != len(employee_ids):
#     print("Duplicates detected")

# for unique_id in unique_employee_ids:
#     for employee_id in employee_ids:
#         if unique_id == employee_id:
#             duplicate_ids.remove(unique_id)
#             break
# print("Duplicate IDs:")
# for dup_id in duplicate_ids:
#     print(dup_id)

# #faster code
# employee_ids = [101, 102, 103, 104, 102, 105, 101, 106]

# seen = set()
# duplicates = set()

# # Find duplicates
# for emp_id in employee_ids:
#     if emp_id in seen:
#         duplicates.add(emp_id)
#     else:
#         seen.add(emp_id)

# # Print results as expected
# print("Duplicate IDs:")
# for dup in duplicates:
#     print(dup)

# erp_employees = {
#     101, 102, 103, 104, 105, 106
# }

# payroll_employees = {
#     101, 102, 104, 106, 107
# }

# missing_in_payroll = erp_employees - payroll_employees

# missing_in_erp = payroll_employees - erp_employees

# synchronized = erp_employees & payroll_employees

# print("Missing from Payroll:")
# for miss_payroll in missing_in_payroll:
#     print(miss_payroll)

# print("Missing from ERP:")
# for miss_erp in missing_in_erp:
#     print(miss_erp)

# print("Synchronized:")
# for sync in synchronized:
#     print(sync)

# data = {
#     "employees": [
#         {"id": 101, "name": "Ahmed", "department": "HR"},
#         {"id": 102, "name": "Sara", "department": "Finance"},
#         {"id": 103, "name": "Irteza", "department": "IT"}
#     ]
# }

# for employee in data["employees"]:
    #print(employee)
    #print(f"{employee["name"]}-{employee["department"]}")

# departments = {
#     "IT": [
#         {"name": "Ahmed", "salary": 1200},
#         {"name": "Irteza", "salary": 1500}
#     ],
#     "HR": [
#         {"name": "Sara", "salary": 1000},
#         {"name": "John", "salary": 1300}
#     ],
#     "Finance": [
#         {"name": "Fatima", "salary": 1800}
#     ]
# }

# for depts,salary in departments.items():
#     total_payroll = 0
#     for sal in salary:
#         total_payroll += sal["salary"]
#     print(f"{depts}: {total_payroll}")

# erp = {
#     "employees": [
#         {"id": 101, "name": "Ahmed", "salary": 1200},
#         {"id": 102, "name": "Sara", "salary": 1500},
#         {"id": 103, "name": "Irteza", "salary": 1800}
#     ]
# }

# payroll = {
#     "employees": [
#         {"id": 101, "name": "Ahmed", "salary": 1200},
#         {"id": 102, "name": "Sara", "salary": 1400},
#         {"id": 104, "name": "John", "salary": 1600}
#     ]
# }

# erp_employees = set()
# payroll_employees = set()

# for employee in erp["employees"]:
#     erp_employees.add(f"{employee["id"]} - {employee["name"]}")
# for employee in payroll["employees"]:
#     payroll_employees.add(f"{employee["id"]} - {employee["name"]}")


# missing_payroll = payroll_employees - erp_employees

# missing_erp = erp_employees - payroll_employees

# print(missing_erp)
# print(missing_payroll)

# for erp_emp in erp["employees"]:
#     for pay_emp in payroll["employees"]:
#         if erp_emp["salary"] != pay_emp["salary"] and erp_emp["name"] == pay_emp["name"] :
#             difference = abs(erp_emp["salary"] - pay_emp["salary"])
#             print(f"""
# {erp_emp["id"]}-{erp_emp["name"]}
# ERP: {erp_emp['salary']}
# Payroll: {pay_emp['salary']}
# Difference: {difference}
#             """)
    

# salaries = [500, 1200, 800, 2000, 1500, 700]

# high_salaries = [number for number in salaries if number > 1000]

# print(high_salaries)

# employees = [
#     {"name": "Ahmed", "salary": 1200, "status": "Active"},
#     {"name": "Sara", "salary": 1500, "status": "Inactive"},
#     {"name": "Irteza", "salary": 1800, "status": "Active"},
#     {"name": "John", "salary": 900, "status": "Active"}
# ]

# active_salaries = [salary["salary"] for salary in employees if salary["status"] == "Active"]

# print(f"active_salaries -> {active_salaries}")

# high_earners = [high_earner["name"] for high_earner in employees if high_earner["salary"] > 1500]

# print(f"high_earners -> {high_earners}")

# employees = [
#     {
#         "id": 101,
#         "name": "Ahmed",
#         "department": "IT",
#         "salary": 1200,
#         "status": "Active"
#     },
#     {
#         "id": 102,
#         "name": "Sara",
#         "department": "HR",
#         "salary": 1500,
#         "status": "Inactive"
#     },
#     {
#         "id": 103,
#         "name": "Irteza",
#         "department": "IT",
#         "salary": 1800,
#         "status": "Active"
#     },
#     {
#         "id": 104,
#         "name": "John",
#         "department": "Finance",
#         "salary": 2200,
#         "status": "Active"
#     }
# ]
# #should use only comprehensions
# active_employee_ids, active_employee_names, it_employee_names = [employee["id"] for employee in employees if employee["status"] == "Active"], [employee["name"] for employee in employees if employee["status"] == "Active"], [employee["name"] for employee in employees if employee["department"] == "IT"]
# print(active_employee_ids)
# print(active_employee_names)
# print(it_employee_names)

# active_high_employees = [employee for employee in employees if employee["status"] == "Active" and employee["salary"] >= 1500 ]

# print(active_high_employees)

# salary_lookup = { emp["id"]:emp["salary"] for emp in employees }
# print(salary_lookup)

# def generate_numbers():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
#     yield 6

# for num in generate_numbers():
#     print(num)

def generate_even_numbers(limit):
    for i in range(limit):
        if i % 2 == 0:
            yield i

for num in generate_even_numbers(10):
    print(num)



















