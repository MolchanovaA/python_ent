import csv


def db_reader_prog_report_creator( month_name:str, dpt = 'any', flag = '-v'): 
    months_numbers_dict = {'January':'01', 'February': '02', 'March' : '03', 'April': '04', 'May': '05', 'June': '06', 'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}
    month_no = months_numbers_dict[month_name.capitalize()]
    with open('database.csv', 'r') as file:
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
            if (len(row) > 0 and row[0] == 'id') or len(row) == 0: 
                continue
            worker_bd_month = row[2][5:7]
            if worker_bd_month == str(month_no) and dpt == row[3].capitalize():
                report['Birthdays'] += 1
                report['BD_DPTS'][dpt] = report['BD_DPTS'].get(dpt, 0) + 1
                if flag == '-v':
                    report['BD_names'].append(row[1])
            worker_ann_month = row[4][5:7]
            if worker_ann_month == str(month_no) and dpt == row[3].capitalize():
                report['Anniversaries'] += 1
                report['Anniv_DPTS'][dpt] = report['Anniv_DPTS'].get(dpt, 0) + 1
                if flag == '-v':
                    report['An_names'].append(row[1])
        print(report, dpt, 'REPORT')
    return report


def report_section_printer(report_s, section_name, section_dpt, names): 
   
    string = f'--- {section_name} ---\n'
    string += f'Total: {report_s[section_name]}\n'
    string += f'By department:\n'
    if len(report_s[section_dpt]) > 0:
        for item in report_s[section_dpt].items(): 
            string += f'- {item[0]} : {item[1]}\n'
    if report_s.get(names, 'Not Exist') != 'Not Exist': 
        string += f'Names: \n'
        for name in report_s.get(names): 
            string += f'** {name}\n'
    return string



def report_printer(_report, _month):
    rep = f'Report for {_month} generated\n'
    bd = report_section_printer(_report, 'Birthdays', 'BD_DPTS', 'BD_names')
    rep += bd
    ann = report_section_printer(_report, 'Anniversaries', 'Anniv_DPTS', 'An_names')
    rep += ann
    return rep

