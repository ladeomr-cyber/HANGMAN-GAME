from words import get_word
from game import play_game

def main():
    while True:
        word = get_word()
        play_game(word)
        choice = input("\nPlay again? (y/n): ").lower()
        if choice != "y":
            break

if __name__ == "__main__":
    main()