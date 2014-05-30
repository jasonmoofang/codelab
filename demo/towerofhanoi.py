def tower_of_hanoi(src, dest, rem, size):
    if size == 1:
        print "move a disk from " + src + " to " + dest
    else:
        tower_of_hanoi(src, rem, dest, size - 1)
        print "move a disk from " + src + " to " + dest
        tower_of_hanoi(rem, dest, src, size - 1)



stacksize = float(raw_input("Enter stack size: "))
tower_of_hanoi("tower 1", "tower 2", "tower 3", stacksize)