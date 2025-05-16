import employee_info as e_i
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():

    y=[]
    for i in employee_data:#the for loop here is impt since you want to keep adding and not just do it once thats why yu do a nested if loop in the for loop
        if i["age"]>=23 and i["age"]<=30:
            y.append(i)
    x=e_i.get_employees_by_age_range(22,31)
    assert(x==y)

def test_calculate_average_salary():
    x=50000 +60000+56000+70000+65000+60000
    avg=(x/6)
    y=e_i.calculate_average_salary()
    assert(avg==y)

def test_get_employees_by_dept():
    y=[]
    for i in employee_data:
        if i["department"]=="sales":
            y.append(i)
    x=e_i.get_employees_by_dept("sales")
    assert(x==y)     
