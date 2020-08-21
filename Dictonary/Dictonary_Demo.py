my_context = {
    "item": {'name': 'John', 'age': '27', 'sex': 'Male'}
}
my_context['name'] = 'Khushi'

print(my_context['item']['name'])  # op:-John
print(my_context['name'])  # Khushi

"""Add Some Key And Values"""

my_context['food'] = 'pizza'

print(my_context)
#op:-{'item': {'name': 'John', 'age': '27', 'sex': 'Male'}, 'name': 'Khushi', 'food': 'pizza'}


data = {1: 'ankit', 2: 'ramesh', 3: 'dinesh',
        4: {
            'key4': ['food', 'drinks']
        }
        }

print(data)
#op:-{1: 'ankit', 2: 'ramesh', 3: 'dinesh', 4: {'key4': ['food', 'drinks']}}

print(data[4])
#op:-{'key4': ['food', 'drinks']}
