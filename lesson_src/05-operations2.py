# Unlike numbers, math operations on strings don't make sense!
# However, we can still concatenate strings

print "Hello " + "World" + "!"

# What if we want to concatenate strings and numbers

# print "I am number " + 1 # this doesn't work!

# Need to convert the number into a string using 'str()'!

print "I am number " + str(1) + "!"

# This lets us concatenate the results of math operations!

print "two plus three is " + str(2 + 3)
print "five times seven is " + str(5 * 7)

# What does this print?
print "1" + str(2)