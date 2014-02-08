# a function is a bundled collection of statements:
def print_greeting():
    print "Hello!"
    print "I don't believe we've met before!"

# Call our function:
print_greeting()
print_greeting()

# a function can "return" a value
def make_greeting():
  return "Hello! I don't believe we've met before!"

# We can assign the returned value to a variable
my_greeting = make_greeting()
print my_greeting

# a function can take "arguments" from the caller
def make_greeting_to(name):
    return "Hello " + name + "! How do you do?"

print make_greeting_to("Bob")
print make_greeting_to("Sue")

# a function can take as many arguments as necessary
def calculate_triangle_area(height, base):
    return height * base / 2

print calculate_triangle_area(5, 6)
print calculate_triangle_area(10, 5)