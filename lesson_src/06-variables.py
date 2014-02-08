# Variables store values
my_first_name = "John"
my_last_name = "Smith"

# Variables can be used in the same way as the value it stores
my_name = my_first_name + " " + my_last_name
print my_name

# Can't do this because my_first_name is a string not a number
# print my_first_name - 7

triangle_height = 10
triangle_base = 12
triangle_area = triangle_height * triangle_base / 2
print triangle_area

# you can change the value of a variable
triangle_height = 15
print triangle_height

# but this does not affect triangle area or any other variable!
print triangle_area

# have to recompute:
triangle_area = triangle_height * triangle_base / 2
print triangle_area