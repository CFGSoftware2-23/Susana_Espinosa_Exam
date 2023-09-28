def triangle_number_non_recursive(n):
    if n <= 0:
        return 0

    triangle_sum = 0
    for i in range(1, n + 1):
        triangle_sum += i

    return triangle_sum


result = triangle_number_non_recursive(4)
print(result)
