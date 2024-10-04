user = input()
user = user.split()

for inputs in user:
    inputs_index = user.index(inputs)
    if inputs_index % 2 == 0:
        user.insert(inputs_index+1, '...')
user.pop()
for inputs in user:
    print(inputs, end="")
print("")
