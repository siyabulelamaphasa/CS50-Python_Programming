users_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

if users_input == "42" or users_input == "forty two" or users_input == "forty-two":
    print("Yes")
else:
    print("No")
