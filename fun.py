def calculate_structure_sum(*args):
    summ = 0
    for element in args:
        if isinstance(element, str):
            summ += len(element)
        elif isinstance(element, int):
            summ += element
        elif isinstance(element, float):
            summ += element
        elif isinstance(element, bool):
            summ += element
        elif isinstance(element, list):
            summ += calculate_structure_sum(*element)
        elif isinstance(element, tuple):
            summ += calculate_structure_sum(*element)
        elif isinstance(element, set):
            summ += calculate_structure_sum(*element)
        elif isinstance(element, dict):
            summ += calculate_structure_sum(*tuple(element.items()))
    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
