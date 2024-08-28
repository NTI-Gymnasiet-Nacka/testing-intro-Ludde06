# Största skillnad

def main():
    text = input()
    text = text.replace(" ", "").split(",")
    tal = []
    for u in text:
        tal.append(int(u))
    print(max(tal)-min(tal))

if __name__ == "__main__":
    main()