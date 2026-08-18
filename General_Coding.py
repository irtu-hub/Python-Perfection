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

# def generate_even_numbers(limit):
#     for i in range(limit):
#         if i % 2 == 0:
#             yield i

# for num in generate_even_numbers(10):
#     print(num)

# def calculate_net_salary(basic_salary, allowance, deduction):
#     gross = basic_salary + allowance
#     return gross - deduction

# net_salary = calculate_net_salary(350, 100, 50)

# print(net_salary)


# valid_emp = {"id": "emp1", "name": "Irteza", "basic_salary": 1200}

# missing_id = {"name": "Ahmed", "basic_salary": 500}

# missing_name = {"id": "emp3", "basic_salary": 600}

# missing_salary = {"id": "emp4", "name": "Masooma"}

# empty_id = {"id": "", "name": "Idrees", "basic_salary": 400}

# zero_salary = {"id": "emp6", "name": "Salim", "basic_salary": 0}

# negative_salary = {"id": "emp7", "name": "Tariq", "basic_salary": -150}

# def validate_employee(employee):
#     if "id" not in employee or "name" not in employee or "basic_salary" not in employee:
#         return False
#     if employee["id"] != "" and employee["name"] != "" and employee["basic_salary"] > 0:
#         return True
#     else:
#         return False

# emp = validate_employee(valid_emp)
# print(emp)

# emp = validate_employee(missing_name)
# print(emp)

# def calculate_invoice(amount, tax=5):
#     return amount - amount * tax/100

# cal = calculate_invoice(100, 2)
# print(cal)

# cal = calculate_invoice(200)
# print(cal)

# def create_employee(
#     name,
#     department,
#     country="Oman",
#     active=True
# ):
#     return{
#         "name": name,
#         "department": department,
#         "country" : country,
#         "active" : active
#     }

# pr = create_employee("irteza", "IT")
# print(pr)
# pr = create_employee("dev", "Sales", "India")
# print(pr)
# pr = create_employee(department="HR", active=False, name="sam", country="US")
# print(pr)

# def calculate_total(*args):
#     return sum(args)

# tot = calculate_total(100, 200)
# print(tot)
# tot = calculate_total(100, 200, 300, 400)
# print(tot)


# def print_employee(**kwargs):
#     print(kwargs)


# print_employee(
#     name="Irteza",
#     department="IT",
#     salary=1500
# )

# def process_transaction(transaction_type, *amounts, **details):
#     total = sum(amounts)
#     print(total, details)


# process_transaction(
#     "invoice",
#     100,
#     200,
#     300,
#     customer="ABC Pharmacy",
#     currency="OMR",
#     approved=True
# )


# employees = [
#     {"name": "Ahmed", "salary": 1200},
#     {"name": "Sara", "salary": 1800},
#     {"name": "Irteza", "salary": 2500}
# ]


# def calculate_tax(salary):
#     return salary * 0.05


# def calculate_bonus(salary):
#     return salary * 0.10


# def calculate_net_salary(salary, calculation):
#     deduction = calculation(salary)
#     return salary - deduction


# calculations = {
#     "tax": calculate_tax,
#     "bonus": calculate_bonus
# }


# def process_employee(employee, calculation):
#     salary = employee["salary"]

#     net_salary = calculate_net_salary(
#         salary,
#         calculation
#     )

#     return {
#         "name": employee["name"],
#         "gross_salary": salary,
#         "net_salary": net_salary
#     }


# for employee in employees:
#     result = process_employee(
#         employee,
#         calculations["tax"]
#     )

#     print(result)

# def calculate_tax(salary, tax):
#     return

# def calculate_bonus(salary, bonus):
#     return salary + bonus

# tax = calculate_tax

# bonus = calculate_bonus



# print(tax(1000, 5))
# print(bonus(1000,25))

# def tax_calculation(salary, tax):
#     return salary * (tax/100)

# def discount_calculation(salary, discount):
#     return salary * (discount/100)

# def bonus_calculation(salary, bonus):
#     return salary * (bonus/100)


# def apply_operation(amount, operation):
#     value = float(input("enter percentage rate"))
#     return operation(amount,value)

# print(apply_operation(1500, tax_calculation))

# def tax_calculation(salary, tax):
#      return salary * (tax/100)

# def comission_calculation(salary, discount):
#      return salary * (discount/100)

# def bonus_calculation(salary, bonus):
#      return salary * (bonus/100)

# rules = {
#     "tax": tax_calculation,
#     "bonus": bonus_calculation,
#     "commission": comission_calculation
# }

# percentages = {
#      "tax": 5,
#      "bonus": 9,
#      "comission": 2
# }


# def process_employee(amount, function):

#     if function is tax_calculation:
#         value = percentages["tax"]
#     elif function is bonus_calculation:
#         value = percentages["bonus"]
#     elif function is comission_calculation:
#         value = percentages["comission"]

#     return function(amount, value)

# print(process_employee(2500, rules["tax"]))
     

# def create_discount_calculator(discount_rate):

#     def discount_calculator(price):
#         return price - price * (discount_rate/100)

#     return discount_calculator

# dis_a = create_discount_calculator(10)
# dis_b = create_discount_calculator(20)

# print(dis_a(10000))
# print(dis_b(10000))


# def create_salary_calculator(allowance):

#     def salary_calculator(basic_salary):
#         return basic_salary + allowance

#     return salary_calculator

# hr_allowance_calculator = create_salary_calculator(300)
# manager_allowance_calculator = create_salary_calculator(700)

# print(hr_allowance_calculator(500))
# print(manager_allowance_calculator(500))

# employee = {
#     "name": "Irteza",
#     "basic_salary": 2000
# }

# def create_payroll_processor(**kwargs):
#     allowance_rate = kwargs.get("allowance_rate", 0)
#     tax_rate = kwargs.get("tax_rate", 0)

#     def calculate(employee):
#         gross_salary = employee["basic_salary"] + employee["basic_salary"] * (allowance_rate/100)
#         net_salary = gross_salary - gross_salary * (tax_rate/100)
#         return (net_salary,gross_salary)
#     return calculate

# omani = create_payroll_processor(allowance_rate = 10,tax_rate = 4)
# expat = create_payroll_processor(allowance_rate =5, tax_rate = 4)

# print(omani(employee))
# print(expat(employee))


# def audit_action(function):

#     def wrapper(*args, **kwargs):
#         print(f"[AUDIT] Starting {function.__name__}")

#         result = function(*args, **kwargs)

#         print(f"[AUDIT] Completed {function.__name__}")

#         return result

#     return wrapper


# @audit_action
# def calculate_net_salary(
#     basic_salary,
#     allowance=0,
#     deduction=0
# ):
#     gross_salary = basic_salary + allowance
#     net_salary = gross_salary - deduction

#     return net_salary


# @audit_action
# def create_employee(name, department):
#     return {
#         "name": name,
#         "department": department
#     }


# salary = calculate_net_salary(
#     basic_salary=1500,
#     allowance=300,
#     deduction=100
# )


# employee = create_employee(
#     name="Irteza",
#     department="IT"
# )

# print(f"Net salary: {salary}")
# print(employee)


# def log_execution(function):

#     def wrapper():
#         print("starting generate_report....")

#         function()

#         print("Finished generate_report.....")

#     return wrapper

# @log_execution
# def generate_report():
#     print("Generating report...")


# generate_report()


# employees = [
#     {
#         "name": "Ahmed",
#         "salary": 1200
#     },
#     {
#         "name": "Sara",
#         "salary": 1500
#     },
#     {
#         "name": "Irteza",
#         "salary": 1800
#     }
# ]


# total_payroll = 0

# with open("payroll_report.txt", "w") as file:
#     file.write("PAYROLL REPORT\n")
#     file.write("--------------------\n")

#     for employee in employees:
#         name = employee["name"]
#         salary = employee["salary"]

#         total_payroll += salary

#         file.write(
#             f"{name}: {salary:.2f} OMR\n"
#         )

#     file.write("--------------------\n")
#     file.write(
#         f"Total Payroll: {total_payroll:.2f} OMR\n"
#     )


# with open("payroll_report.txt", "r") as file:
#     report = file.read()


# print(report)

# employees = ["john", "Ghafoor", "silesh", "Akmaisuchi", "ghanrafi"]

# with open("employees.txt", "w") as names :
#     for employee in employees:

#         names.write(f"{employee}\n")

# with open("employees.txt", "r") as file :
#     names = file.read()
# print(names)


# with open("transactions.txt", "r") as file:
#     total_transactions = 0
#     no_of_transactions = 0
#     transactions_1500 = 0
#     for line in file:
#         transactions = int(line.strip())
#         total_transactions += transactions
#         no_of_transactions += 1
#         if transactions >= 1500:
#             transactions_1500 += 1
#     with open("transaction_summary.txt", "w") as file:
#         file.write(f"{total_transactions}\n")
#         file.write(f"{no_of_transactions}\n")
#         file.write(f"{transactions_1500}\n")



# with open("record.txt", "r") as file:
#     datas = []
#     errors = []
#     total = 0
#     invalid = 0
#     for line in file:
#         total += 1
#         cleaned_line = line.strip()
#         datas.append(cleaned_line.split(","))
#     print
#     for i,data in enumerate(datas, start =1):
#         if len(data)< 3 :
#             invalid += 1
#             errors.append({
#                   f"Line {i}": "Invalid record structure"  
#                 })
#         elif not int(data[2]) > 0:
#             invalid += 1
#             errors.append({
#                 f"Line {i}" : "Invalid salary"
#             }) 
#     with open("import_report.txt", "w") as file:
#         file.write(f"""
#     ERP IMPORT REPORT

#     Total: {total}
#     Valid: {total - invalid}
#     Invalid: {invalid}

#     Errors:\n""")   
#         for error in errors:
#             for line, err in error.items():
#                 file.write(f"   {line}:{err}\n")         



# from pathlib import Path

# path = Path("reports") / "payroll"

# path.mkdir(
#     parents = True,
#     exist_ok= True
# )

# report_path = path / "report.txt"

# report_path.touch()

# if path.exists():
#     print("File exists")
# else:
#     print("File doesnt exist")

# from pathlib import Path

# files = [
#     "invoice.pdf",
#     "employees.csv",
#     "policy.txt",
#     "payroll.xlsx",
#     "contract.pdf"
# ]

# #path = Path(files)

# for file in files:
#     if Path(file).suffix == ".pdf" :
#         print(file)

# from pathlib import Path


# # file = Path("seq_det.v")

# # print("Path:")
# # print(file)

# # print("\nAbsolute Path:")
# # print(file.absolute())
# #file = Path("The Quran and its interpreters - Vol 1.pdf")

# file_location = Path(r"d:\code\Linux_Commands_Cheat_Sheet.pdf")

# with open(file_location, "rb") as pdf_file:
#     content = pdf_file.read()
#     print(content)

# import json
# invoice = {
#     "invoice_id": "INV-1001",
#     "customer": "ABC Pharmacy",
#     "amount": 1250.500,
#     "paid": False
# }

# json_data = json.dumps(invoice)

# print(json_data)
# print(type(json_data))

# from pathlib import Path
# import json

# purchase_requests = [
#     {
#         "request_id": "PR-2026-001",
#         "department": "Marketing",
#         "amount": 1250.00,
#         "approved": True
#     },
#     {
#         "request_id": "PR-2026-002",
#         "department": "Engineering",
#         "amount": 8400.00,
#         "approved": False
#     },
#     {
#         "request_id": "PR-2026-003",
#         "department": "Human Resources",
#         "amount": 450.00,
#         "approved": True
#     },
#     {
#         "request_id": "PR-2026-004",
#         "department": "Operations",
#         "amount": 3120.00,
#         "approved": True
#     },
#     {
#         "request_id": "PR-2026-005",
#         "department": "Sales",
#         "amount": 950.00,
#         "approved": False
#     }
# ]

# exports = Path("exports")

# exports.mkdir(exist_ok= True)

# purchase_file = exports / "purchase_requests.json"

# with purchase_file.open("w") as file:
#     json.dump(purchase_requests, file, indent= 4)


# with purchase_file.open("r") as file:
#     imported_purchase_requests = json.load(file)

# total_requests = 0
# total_approved_amount = 0
# approved_requests = []
# rejected_requests = []
# for purchase_requests in imported_purchase_requests:
#     total_requests += 1
#     if purchase_requests["approved"] == True:
#         approved_requests.append(purchase_requests)
#         total_approved_amount += purchase_requests["amount"]
#     elif purchase_requests["approved"] == False:
#         rejected_requests.append(purchase_requests)
    
# print(total_requests)
# print(total_approved_amount)     
# print(approved_requests)
# print(rejected_requests)

# from pathlib import Path
# import csv

# sales_csv = Path("sales.csv")

# with sales_csv.open("r", newline= "", encoding= "utf-8") as file :
#     reader = csv.DictReader(file)
#     amount = 0
#     for data in reader:
#         amount += float(data["amount"])
        
# print(amount)

# from pathlib import Path
# import csv

# salary_file = Path("employee_salaries.csv")

# with salary_file.open("r", newline="", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     total_employees = 0
#     highest_paid = 0
#     total_payroll = 0
#     High_pay = []
#     for employee in reader:
#         total_employees +=1
#         total_payroll += float(employee["salary"])
#         if highest_paid <= float(employee["salary"]):
#             highest_paid = float(employee["salary"])
#             highest_paid_emp = employee["First_Name"] + employee["Last_Name"]
#         if float(employee["salary"]) > 80000 :
#             High_pay.append(employee)
#         avg_salary = total_payroll/total_payroll
    

# with open("Summary.txt", "w") as file:
#     file.write(f"""
# ================
# SUMMARY
# ================
# Total employees : {total_employees}
# Total payroll : {total_payroll}
# Average salary : {avg_salary}
# Highest-paid employee : {highest_paid_emp}
# Employees earning > 1000 : {High_pay}
# -----------------------
# """)

# from pathlib import Path
# import csv
# #aphro, d3vit,electro, irofizz,vitmiad,wom,znkc,biotina
# file_loc = Path("S3_ZULULAN_PHARMA_202608.csv")

# with file_loc.open("r", newline= "", encoding= "utf-8") as file:
#     reader = csv.DictReader(file)
#     found = []
#     item_names = set()
#     months = ["Jan", "Feb","Mar","Apr", "May", "Jun", "Jul"]
#     aph = {m:0.0 for m in months}
#     d3_vit = {m:0.0 for m in months}
#     elect = {m:0.0 for m in months}
#     iro = {m:0.0 for m in months}
#     vitad = {m:0.0 for m in months}
#     vitwo = {m:0.0 for m in months}
#     znk = {m:0.0 for m in months}
#     bio = {m:0.0 for m in months}
# #total = sum(float(product[m]) + float(product[f"{m} Foc"]) for m in months)

#     for data in reader:
#         if "branch" in data["CustName"].lower() and not "NABORS" in data["CustName"] :
#             found.append(data)
#             item_names.add(data["Item Desc"])
#     for product in found:
#         for m in months:
#             match(product["Item Desc"]):
                
#                 case "APHROVIT":
#                     aph[m] += float(product[f"{m}"]) + float(product[f"{m} Foc"]) 

#                 case "D3-VIT" :
#                     d3_vit[m] += float(product[f"{m}"]) + float(product[f"{m} Foc"]) 

#                 case "ELECTROBIOTICA":
#                     elect[m] += float(product[f"{m}"]) + float(product[f"{m} Foc"]) 


#                 case "IROFIZZ" :
#                     iro[m] += float(product[f"{m}"]) + float(product[f"{m} Foc"]) 


#                 case "VITMI-ADULTS" :
#                     vitad[m] += float(product[f"{m}"]) + float(product[f"{m} Foc"]) 


#                 case "VITMI WOMEN" :
#                     vitwo[m] += float(product[f"{m}"]) + float(product[f"{m} Foc"]) 


#                 case "ZINK C" :
#                     znk[m] += float(product[f"{m}"]) + float(product[f"{m} Foc"]) 


#                 case "BIOTINA (ORANGE FLAVOUR)" :
#                     bio[m] +=float(product[f"{m}"]) + float(product[f"{m} Foc"]) 

# with open("muscat_pharmacy_report.txt", "w") as file:
#     for m in months:
#     file.write(f"""
# ============================================================
# REPORT FOR ASKED PRODUCTS SALES BY MUSCAT PHARMACY BRANCHES
# ============================================================

# APHROVIT : {aph}

# D3-VIT : {d3_vit}

# ELECTROBIOTICA : {elect}

# IROFIZZ : {iro}

# VITMI-ADULTS : {vitad}

# VITMI WOMEN : {vitwo}

# ZINK C : {znk}

# BIOTINA (ORANGE FLAVOUR) : {bio}

#     """)





        








































