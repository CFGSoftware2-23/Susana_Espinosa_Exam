class MyCustomLength:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        if isinstance(self.data, int):
            return len(str(abs(self.data)))
        else:
            return len(self.data)


# Test cases
my_list = [1, 2, 3, 4, 5]
my_set = {10, 20, 30}
my_string = "Hello, Susana!"
my_integer = 12345

custom_list = MyCustomLength(my_list)
custom_set = MyCustomLength(my_set)
custom_string = MyCustomLength(my_string)
custom_integer = MyCustomLength(my_integer)

print("Custom Length of List:", len(custom_list))
print("Custom Length of Set:", len(custom_set))
print("Custom Length of String:", len(custom_string))
print("Custom Length of Integer:", len(custom_integer))
