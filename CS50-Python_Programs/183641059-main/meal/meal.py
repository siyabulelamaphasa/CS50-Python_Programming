def main():
    time = input("What time is it? ").strip()
    if convert(time) >= 7.0 and convert(time) <= 8.0:
        print("breakfast time")
    elif convert(time) >= 12.0 and convert(time) <= 13.0:
        print("lunch time")
    elif convert(time) >= 18.0 and convert(time) <= 19.0:
        print("dinner time")
    else:
        return


def convert(time):
    a, b = time.split(":")
    hour = float(a)
    minutes = float(b) * 1 / 60
    return float(hour+minutes)


if __name__ == "__main__":
    main()
