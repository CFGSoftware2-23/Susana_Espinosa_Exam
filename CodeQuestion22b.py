def triangle_number_recursive(n):
    if n <= 0:
        return 0
    else:
        return n + triangle_number_recursive(n - 1)


result = triangle_number_recursive(4)
print(result)
