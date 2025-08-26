sentence = input("Enter a sentence: ")

while True:
    print("\nChoose an operation:")
    print("1. Reverse the sentence")
    print("2. Count vowels")
    print("3. Check if palindrome")
    print("4. Find and replace a word")
    print("5. Format (title case)")
    print("6. Split into words")
    print("7. Word frequency counter")
    print("8. Swap case")
    print("9. Exit")
    print("0. Enter a new sentence")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Reversed:", sentence[::-1])

    elif choice == "2":
        vowels = "aeiouAEIOU"
        count = 0
        for ch in sentence:
            if ch in vowels:
                count += 1
        print("Vowel count:", count)

    elif choice == "3":
        clean = "".join(c.lower() for c in sentence if c.isalnum())
        if clean == clean[::-1]:
            print("Palindrome? Yes")
        else:
            print("Palindrome? No")

    elif choice == "4":
        find_word = input("Word to find: ")
        replace_word = input("Word to replace with: ")
        sentence = sentence.replace(find_word, replace_word)
        print("Updated sentence:", sentence)

    elif choice == "5":
        sentence = sentence.title()
        print("Formatted:", sentence)

    elif choice == "6":
        print("Words:", sentence.split())

    elif choice == "7":
        words = sentence.lower().split()
        freq = {}
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
        print("Word frequency:", freq)

    elif choice == "8":
        print("Swapped case:", sentence.swapcase())

    elif choice == "9":
        print("Exiting program. Goodbye!")
        break

    elif choice == "0":
        sentence = input("Enter a new sentence: ")

    else:
        print("Invalid choice, try again.")
