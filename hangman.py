import random

def get_random_word():
    words = ["python", "java", "javascript", "hangman", "programming", "january", "zachary", "watch", "keyboard", "controller", "computer", "university", "sunglasses"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    while True:
        word = get_random_word()
        guessed_letters = set()
        attempts = 6
        total_guesses = 0
    
        print("Welcome to Zach's Hangman!")
        print("You have 6 attempts to guess the word.")
    
        while attempts > 0:
            print(f"\nWord: {display_word(word, guessed_letters)}")
            guess = input("Guess a letter: ").lower()
            total_guesses += 1
        
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please guess a single letter.")
                continue
        
            if guess in guessed_letters:
                print("You've already guessed that letter.")
                continue
        
            guessed_letters.add(guess)
        
            if guess in word:
                print(f"Good guess! '{guess}' is in the word.")
            else:
                attempts -= 1
                print(f"Wrong guess. '{guess}' is not in the word. Attempts left: {attempts}")
        
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You guessed the word: {word} in {total_guesses} total guesses!")
                break
        else:
            print(f"\nSorry, you ran out of attempts. The word was: {word}")

        another = input("Would you like to play again? ")
        if another.lower() == "yes":
            continue
        else:
            print("Have a nice day and thanks for playing!")
            break

if __name__ == "__main__":
    play_hangman()