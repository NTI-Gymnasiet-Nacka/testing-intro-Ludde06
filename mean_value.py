# Medelvärde

def main():
    text = input()
    text = text.replace(" ", "").split(",")
    tal = []
    for u in text:
        tal.append(int(u))
    print(f'{sum(tal)/len(tal)}')

if __name__ == "__main__":
    main()
