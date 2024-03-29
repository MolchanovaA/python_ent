from faker import Faker
import csv
import random
fake = Faker()


def random_data_generator(id_number, list_of_columns):
    randomUser = {'id': id_number}
    departments = ['HR', 'Admin', 'Engineering', 'IT', 'Security']
    for column in list_of_columns: 
        if column == 'Name': 
            randomUser[column] = fake.name()
        elif column == 'Birthday': 
            randomUser[column] = fake.date_of_birth(minimum_age = 20, maximum_age = 60)
        elif column == 'Hiring date': 
            randomUser[column] = fake.date_between(start_date = '-2y')
        elif column == 'Department':
            total_DPT = len(departments) - 1
            randDPT = random.randint(0, total_DPT) 
            randomUser[column] = departments[randDPT]
    return randomUser

with open('database.csv', 'w') as file:
    column_names = ['id', 'Name', 'Birthday', 'Department', 'Hiring date']
    writer = csv.DictWriter(file, fieldnames=column_names)
    writer.writeheader()
    number_of_users = 10
    for id in range(number_of_users):
        user = random_data_generator(id, column_names)
        writer.writerow(user)
