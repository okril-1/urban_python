def count_numbers_and_strings(*args):
    total_sum = 0
    total_length = 0

    def recursive_count(data):
        nonlocal total_sum, total_length

        for item in data:
            if isinstance(item, list):
                recursive_count(item)
            elif isinstance(item, dict):
                for key, value in item.items():
                    recursive_count([key, value])
            elif isinstance(item, tuple):
                recursive_count(item)
            elif isinstance(item, str):
                total_length += len(item)
            elif isinstance(item, (int, float)):
                total_sum += item

    recursive_count(args)

    return total_sum, total_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = count_numbers_and_strings(data_structure)
print(result)  # Output: (34, 10)
