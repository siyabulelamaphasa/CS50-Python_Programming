camel_case = input("Enter the camelCase: ")
print("snake_case: ", end="")

for characters in camel_case:
    if characters.islower():
        print(characters, end="")
    if characters.isupper():
        print("_", characters.lower(), end="", sep="")

print()
