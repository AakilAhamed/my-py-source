# LIST
x = [1, 2, 3, 4]
print(f"\nlist = {x}")
# add element
x.append("Five")
print(f"after appending 'Five' = {x}")
# insert element
x.insert(2, "inserted")
print(f"after insertion = {x}")
# remove an element
x.remove(2)
print(f"after removal = {x}")
# Delete
del x[1]
print(f"after deletion = {x}")


# Tuple
y = (1, 2, 3, 4)
print(f"\n\nTuple = {y}")
# creating a new tuple with modifications
# adding an elemnet
y = y + (5,)
print(f"adding an element = {y}")
# inseting an element
y = y[:2] + ("inserted",) + y[2:]
print(f"after insertion = {y}")
# deleting an element
y = y[:2] + y[3:]
print(f"after deletion = {y}")

# Dictionary
z = {"name": "Aakil", "age": 23, "city": "Liberty City"}
print(f"\n\ndictionary = {z}")
# Add
z["occupation"] = "Cowboy"
print("after addition:", z)
# Modify
z["age"] = 31
print("after modifying:", z)
# Delete
del z["city"]
print("after deleting:", z)