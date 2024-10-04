def convert(inputs):
    if inputs == ":)":
        return "🙂"
    else:
        return "🙁"

def main():
    print("", end="")
    text = input().split()
    for texts in text:
        if texts == ":)" or texts == ":(":
            text_index = text.index(texts)
            text[text_index] = convert(texts)
    print("", end="")
    for texts in text:
        print(texts, end=" ")
    print("")

if __name__ == "__main__":
    main()
