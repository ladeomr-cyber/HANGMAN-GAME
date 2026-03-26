def play_game(word):
    guessed = set()
    attempts = 6
    display = ["_"] * len(word)

    while attempts > 0 and "_" in display:
        print("\nWord:", " ".join(display))
        print("Attempts left:", attempts)
        guess = input("Enter a letter: ").lower()

        if guess in guessed:
            print("Already guessed")
            continue

        guessed.add(guess)

        if guess in word:
            print("Correct guess")
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("Wrong guess")
            attempts -= 1

    if "_" not in display:
        print("\nYou won! Word was:", word)
    else:
        print("\nYou lost! Word was:", word)