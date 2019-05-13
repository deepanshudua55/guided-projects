d = {}

d = {'foo': 'bar'}

print(d.values())

print(d['foo'])

for key in d:
    print(f'{key} is {d[key]}')

for k, v in d.items():
    print(f'{k} is {v}')
