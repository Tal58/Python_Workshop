from timeit import timeit
def list_comp():
    return [i for i in range(1000000)]
size = 100
time_list_comp = timeit(list_comp, number = size)

def for_loop():
    result = []
    
    for i in range(1000000):
        result.append(i)
    return result
size = 100
time_for = timeit(for_loop, number = size)

print(f"{time_for:.2f} is time for  {time_list_comp:.2f} is list comp")