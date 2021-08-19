first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха',
           'была', '+5', 'градусов']

second_list = []
for elem in first_list:
    if elem.isdigit():
        second_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        second_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        second_list.append(elem)

out_info = ' '.join(second_list)
print(out_info)
