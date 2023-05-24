import timeit

start_time = timeit.default_timer()

for i in range(1, 1_000_000):
    i**2

end_time = timeit.default_timer()

execution_time = (end_time - start_time) * 1000  # in milliseconds
print(f"Execution time: {execution_time} ms")