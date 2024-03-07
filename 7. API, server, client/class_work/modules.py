import csv

def get_info_from_db(key= None, value= None):
    list_of_books = []
    with open ('db_info.csv', 'r') as f:
        reader = csv.DictReader(f)
        for item in reader:
            if key == None and value == None:
                list_of_books.append(item)
            elif item[key] == value:
                list_of_books.append(item)

    # print(list_of_books)
    return list_of_books