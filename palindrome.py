# Palindrome

def main():
    text = input("")
    if text[::-1] == text:
        print(True)
    else:
        print(False)

if __name__ == "__main__":
    main()
