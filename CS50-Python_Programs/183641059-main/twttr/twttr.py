text = input("Please enter a string of text: ")
text = text.strip()
vowels = "aeiouAEIOU"

not_vowels = ''.join(char for char in text if char not in vowels)
print(not_vowels)
