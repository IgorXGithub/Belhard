def read_csv(file):
    with open(file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        data_list = []
        for line in lines[1:]:
            values = line.strip().split(',')
            row_dict = {headers[i]: values[i] for i in range(len(headers))}
            data_list.append(row_dict)
    return print(data_list)

read_csv('res.csv')
