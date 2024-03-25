import unittest
from unittest.mock import Mock
import csv


# function

def temp_converter( temp_arg:int, unit:str):
    temp = int(temp_arg)
    if isinstance(temp, int) != True and isinstance(unit, str) != True:
        raise TypeError
    return  (temp - 32) * 5 / 9 if unit.lower() == 'c' else temp*9/5 + 32

def get_temp_data_from_file(file) -> list:
    data_collector = []
    with open(file, 'r') as f:
        reader = csv.reader(f)
        convert_to = 'c'
        next(reader) 
        for line in reader:
            temp = float(line[0])
            corrected_temp = temp_converter(temp, convert_to)
            data_collector.append(corrected_temp)

    return data_collector


def save_to_csv(file, data_list:list):
    data = data_list[:]
    if len(data) <= 0:
        raise TypeError
    
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Temperature (C)'])
        for i in data:
            writer.writerow([i])


def statistic_reader(data_list:list):
    stat_list = data_list[:]
    average_t = sum(stat_list) / len(stat_list)
    min_t = min(stat_list)
    max_t = max(stat_list)

    print("Statistics:")
    print("Average: {:.2f}°C".format(average_t))
    print("Minimum: {:.2f}°C".format(min_t))
    print("Maximum: {:.2f}°C".format(max_t))


def process_data(f1, f2):
    collected_temps = get_temp_data_from_file(f1)
    statistic_reader(collected_temps)
    save_to_csv(f2, collected_temps)


# test 
    
test_file = 'test.csv'
rows = [
    ['11'],
    ['22'],
    ['33']
]
    
class UnitTestCase(unittest.TestCase):
    def setUp(self):
        with open(test_file, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file, dialect='excel')
            writer.writerows(rows)

    def test_temp_converter(self):
        temp_c = 10
        convert_to = 'f'
        expected = 50
        result = temp_converter(temp_c, convert_to)
        self.assertEqual(result, expected, 'test_temp_converter')

    def test_statistic_reader(self):
        data_list_test_before = [10,20,30]
        data_list_test_after = [10,20,30]
        statistic_reader(data_list_test_before)
        self.assertListEqual(data_list_test_before, data_list_test_after)

    def test_get_temp_data_from_file(self):
        with open(test_file, 'r') as csv_file:
            reader = csv.reader(csv_file, dialect='excel')
            self.assertEqual(next(reader), rows[0])
            self.assertEqual(next(reader), rows[1])


class IntegrationTestCase(unittest.TestCase):
    
    def test_process_data(self):
        process_data(test_file, 'test_file2.csv')



unittest.main()