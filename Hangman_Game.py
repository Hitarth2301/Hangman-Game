import random
def play_hangman():
    word_list=["python", "developer", "hangman", "programming", "computer", "algorithm"]
    secret_word=random.choice(word_list)
    guessed_display=["_" for _ in secret_word]
    guessed_letters=[]
    lives = 6
    print("Welcome to the Hangman")
    print(f"The word have{len(secret_word)} letters.")
    while lives > 0 and "_" in guessed_display:
        print("\n-----------------------------------------")
        print("Word: " + " ".join(guessed_display))
        print(f"Lives remaining:{lives}")
        print(f"Guessed letters are:{','.join(guessed_letters)}")
        guess = input("Guess a letter:").lower()
        if not guess.isalpha() or len(guess)!= 1:
            print("Please enter a single alphabetical letter.")
            continue 
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        guessed_letters.append(guess)
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            for index in range(len(secret_word)):
                if secret_word[index] == guess:
                    guessed_display[index] = guess
        else:
            print(f"Wrong '{guess}' is not in the word.")
            lives -= 1
    print("\n-----------------------------------------")
    if "_" not in guessed_display:
        print(f"Congratulations, You guessed the word: {secret_word}")
    else:
        print(f"Game Over, You ran out of lives. The word was: {secret_word}")
play_hangman()