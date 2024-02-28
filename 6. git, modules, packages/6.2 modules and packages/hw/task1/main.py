import csv
import sys
from package import F_C, C_F, Ft_M, M_Ft


# from temperature import from_C_to_F as C_F, from_F_to_C as F_C
# from distance import distance_F_to_M as F_M, distance_M_to_F as M_F

def converter(target_t: str, temp_convert, target_d, dist_convert):
    with open('file_with_temp.csv') as file: 
        reader = csv.reader(file)
        with open('converted.csv', 'w') as output_file:
            writer = csv.writer(output_file)
            for i, row in enumerate(reader): 
                if i == 0:
                    writer.writerow(row)
                    continue
                result_row = []
                date = row[0]
                result_row.append(date)
                #distance check
                dist = row[1]
                dist_value = dist[:-1] if row[1].endswith('m') else dist[:-2]
                dist_meas_in_file = 'm' if dist.endswith('m') else 'ft'
                if target_d == dist_meas_in_file:
                    result_row.append(dist)
                else: 
                    converted_distance = dist_convert(int(dist_value))
                    result_row.append(converted_distance)

                # temperature check
                temp = row[2]
                temp_val = int(row[2].split('°')[0][:-1])
                temp_meas_in_file = row[2].split('°')[1]                
                if target_t == temp_meas_in_file: 
                    result_row.append(temp)
                else: 
                    converted_temp = int(temp_convert(temp_val))
                    result_row.append(f'{str(converted_temp)}°{target_t}')
                writer.writerow(result_row)



target_temp = sys.argv[1]
target_dist = sys.argv[2]
callback_temp = F_C if target_temp == 'C' else C_F
callback_dist = Ft_M if target_dist == 'm' else M_Ft


if __name__ == '__main__':
    converter(target_temp, callback_temp, target_dist, callback_dist)


