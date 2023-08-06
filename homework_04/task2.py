def func(**kwargs):
    result = {}
    
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

print(func(res=1, reverse=[1, 2, 3]))