my_dict = {'Alex': 1985, 'Vadim': 1991, 'Kira': 2020}
print(my_dict)
print(my_dict['Vadim'])
print(my_dict.get('Polina'))
my_dict.update({'Polina': 2001, 'Denis': 1995})
c = my_dict.pop('Kira')
print(c)
print(my_dict)
my_set = {'Множество', 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5}
print(my_set)
my_set.add(99.99)
my_set.add((6, 5, 3.14))
my_set.discard(4)
print(my_set)