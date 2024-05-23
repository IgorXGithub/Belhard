from yaml import safe_load

with open('builds.yaml', 'r') as builds, open('tasks.yaml', 'r') as tasks:
    data = safe_load(builds)
    data1 = safe_load(tasks)


def find_all_tasks(data: dict, data1: dict, builds_name: str):
    tasks = []
    temp_data = data.get('builds')
    temp_data1 = data1.get('tasks')
    for item in temp_data:
        if item.get('name') == builds_name:
            temp_tasks = item.get('tasks')
            for item1 in temp_data1:
                if item1.get('name') in temp_tasks and item1.get('dependencies'):
                    tasks.extend(item1.get('dependencies'))

    for i in tasks:
        for item in temp_data1:
            if i == item.get('name') and item.get('dependencies') and item.get('dependencies'):
                tasks.extend(item.get('dependencies'))


    temp_tasks.extend(tasks)
    count = len(temp_tasks)
    return f"Список задач для  {builds_name} в количестве {count} - {temp_tasks}"


print(find_all_tasks(data, data1, 'forward_interest'))
