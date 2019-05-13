def example_func(num):
    for i in range(num):
        print(i)


example_func(10)

a = ['a', 'b', 'c']


def add_to_list(added_list):
    new_list = added_list.copy()
    new_list.append(1)
    print(new_list)


add_to_list(a)

print(a)
