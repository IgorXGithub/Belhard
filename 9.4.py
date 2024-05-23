from yaml import safe_load

with open('builds.yaml', 'r') as builds, open('tasks.yaml', 'r') as tasks:
    data = safe_load(builds)
    data1 = safe_load(tasks)


print(data)
print(data1)


