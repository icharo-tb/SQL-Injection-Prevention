def tuple_conversion(employees):

    name, surname, age, department = employees.split('\n')
    return name,surname,int(age),department


print(tuple_conversion('employee_data.txt'))