# creation of the set animals and fruit 
example = {'apple', 'nobady','banana', 'cherry'}
animal ={'dog','girafe','cat','nobady'}

# membership test to verify if 'apple' is in the set
print('apple' in example)

# to see the element that are in both sets
print(animal.intersection(example))

print(animal.difference(example))