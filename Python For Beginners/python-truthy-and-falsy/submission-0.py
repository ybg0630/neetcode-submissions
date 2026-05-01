def is_truthy(value) -> str:
    # False
    if value == "" or value == float(0.0) or value == int(0) or value == False:
        return "Falsy"
    else:
        return "Truthy"





# don't modify code below this line
print(0, "is", is_truthy(0))
print(10, "is", is_truthy(10))

print(0.0, "is", is_truthy(0.0))
print(10.0, "is", is_truthy(10.0))

print("empty str", "is", is_truthy(""))
print("non-empty str", "is", is_truthy("non-empty str"))
