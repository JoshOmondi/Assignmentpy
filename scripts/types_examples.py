def create_data_dict():
    return {
        "name": "Alice",
        "age": 25,
        "grades": [85, 90, 92],
        "courses": ("Math", "Science"),
        "address": {"city": "Lagos", "zip": 100001}
    }

def cast_examples():
    num_str = "10"
    num_int = int(num_str)
    num_float = float(num_int)
    num_str2 = str(num_float)
    my_list = [1, 2, 3]
    my_tuple = tuple(my_list)
    my_new_list = list(my_tuple)
    
    return num_int, num_float, num_str2, my_tuple, my_new_list
