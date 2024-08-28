# Vokalräkning

def main():
    text = input()
    vokaler = 0
    voklerna = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
    for t in text:
        if t.lower() in voklerna:
            vokaler += 1
    print(vokaler)

if __name__ == "__main__":
    main()
