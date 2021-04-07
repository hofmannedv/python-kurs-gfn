shoppingCart = [5, "apple", "banana", "kiwi"]
for element in shoppingCart:
    if type(element) is int:
        print(element)
    else:
        print(element + " ist kein integer")

# Alternativ
for element in shoppingCart:
    if isinstance(element, int):
        print(element)
    else:
        print(element + " ist kein integer")
