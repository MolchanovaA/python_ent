import csv
import sys



def data_collector(row_id: int, report_section, report_dpt, report_main, _row, _month_no): 
     if len(_row) > 0 and _row[row_id][5:7] == _month_no:
            report_main[report_section] += 1
            if report_main[report_dpt].get(_row[3], 'Not Added') == 'Not Added': 
                report_main[report_dpt][_row[3]] = 1
                if report_main.get('BD_names' , 'Not exist') != 'Not exist' and report_section == 'Birthdays': 
                    report_main['BD_names'].append(_row[1])
                if report_main.get('An_names' , 'Not exist') != 'Not exist' and report_section == 'Anniversaries': 
                    report_main['An_names'].append(_row[1])

            else: 
                report_main[report_dpt][_row[3]] += 1
            

def db_reader_prog_report_creator(file_name, month_no, flag = '-v'): 
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        report = {
            'Birthdays': 0,
            'BD_DPTS':  {},
            'Anniversaries': 0,
            'Anniv_DPTS' : {}
        }
        if flag == '-v': 
            report['BD_names'] = []
            report['An_names'] = []
        for row in reader: 
            if len(row) > 0 and row[0] == 'id': 
                continue
            data_collector(2, 'Birthdays', 'BD_DPTS', report, row, month_no)
            data_collector(4, 'Anniversaries', 'Anniv_DPTS', report, row, month_no)
    return report


def report_section_printer(report_s, section_name, section_dpt, names): 
    print(f'--- {section_name} ---')
    print(f'Total: {report_s[section_name]}')
    print(f'By department:')
    if len(report_s[section_dpt]) > 0:
        for item in report_s[section_dpt].items(): 
            print(f'- {item[0]} : {item[1]}')
    if report_s.get(names, 'Not Exist') != 'Not Exist': 
        print(f'Names: ')
        for name in report_s.get(names): 
            print(f'** {name}')



def report_printer(_report, _month): 
    print(f'Report for {_month} generated')
    report_section_printer(_report, 'Birthdays', 'BD_DPTS', 'BD_names')
    report_section_printer(_report, 'Anniversaries', 'Anniv_DPTS', 'An_names')





month = sys.argv[1] or 'August'
db_file_name = sys.argv[2] or 'database'

names_flag = None

try : 
    names_flag = sys.argv[3]
except: 
    print('FAIL')


months_numbers_dict = {'January':'01', 'February': '02', 'March' : '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
month_number = months_numbers_dict[month]
_report_ = db_reader_prog_report_creator(f'{db_file_name}.csv', month_number, names_flag)


report_printer(_report_, month)

