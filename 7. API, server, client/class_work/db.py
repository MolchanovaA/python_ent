import csv

books = [
    {'id': 1, 'author': 'Jack London', 'title': 'Book 1'},
    {'id': 2, 'author': 'Jack London', 'title': 'Book 2'},
    {'id': 3, 'author': 'Jack Sand', 'title': 'Book 1'},
    {'id': 4, 'author': 'William London', 'title': 'Book 1'},
    {'id': 5, 'author': 'William London', 'title': 'Book 2'},
]


with open('db_info.csv', 'w') as f:
    headers = ['id', 'author', 'title']
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    for item in books:
        writer.writerow(item)