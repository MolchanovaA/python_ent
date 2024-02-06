def get_triangle_numbers(list_size: int) -> list:
    general_list = []
    row_generator = []

    for x in range(1, list_size+1):
        for rg in range(1, x+1):
            if rg == 1 or rg == x:
                row_generator.append(1)
            else: 
                magic_num = general_list[x-2][rg - 1] + general_list[x-2][rg - 2]
                row_generator.append(magic_num)
        general_list.append(row_generator)
        row_generator= []

    return general_list


triangle = get_triangle_numbers(5)


def paint_triangle(triangle_list: list):
    triangle_len = len(triangle_list)*2 #10
    for x in triangle_list:
        whitespaces = (triangle_len - len(x)*2)/2
        stringed = [str(c)+' ' for c in x]
        line = ''.join(stringed)
        print(int(whitespaces)*' ', line)


paint_triangle(triangle)