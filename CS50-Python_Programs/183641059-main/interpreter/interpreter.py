values = input("Enter values: ").strip()
x, y, z = values.split(" ")

value_x = x
value_z = z

if y == "+":
    results = float(value_x) + float(value_z)
    print(f"{results:.1f}")
elif y == "-":
    results = float(value_x) - float(value_z)
    print(f"{results:.1f}")
elif y == "*":
    results = float(value_x) * float(value_z)
    print(f"{results:.1f}")
elif y == "/":
    results = float(value_x) / float(value_z)
    print(f"{results:.1f}")
