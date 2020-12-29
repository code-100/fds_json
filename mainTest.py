import JSONDatastore as A

A.create("a", 12)
A.read("a")
A.delete("a")


# This is the Create function with the timer.
A.create("b", 10, 12)
A.read("b")

# After waiting for 12 seconds.
A.read("b")
A.delete("b")