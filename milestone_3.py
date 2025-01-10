while True:
    def check_guess(guess):
        # Convert the guess into lower case
        guess = guess.lower()
        
        # Assuming the secret word is defined somewhere in your code
        secret_word = "apple"
        
        # Check if the guess is in the word
        if guess in secret_word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")

    def ask_for_input():
        while True:
            # Ask the user to guess a letter
            guess = input("Guess a letter: ")
            
            # Check that the guess is a single alphabetical character
            if guess.isalpha() and len(guess) == 1:
                # If the guess passes the checks, break out of the loop
                check_guess(guess)
                break
            else:
                # If the guess does not pass the checks, print a message
                print("Invalid letter. Please, enter a single alphabetical character.")

    # Call the ask_for_input function to test your code
    ask_for_input()
    # Assuming the secret word is defined somewhere in your code
    secret_word = "apple"

    # Step 1: Create an if statement that checks if the guess is in the word
    if guess in secret_word:
        # Print a message saying "Good guess! {guess} is in the word."
        print(f"Good guess! {guess} is in the word.")
    else:
        # Print a message saying "Sorry, {guess} is not in the word. Try again."
        print(f"Sorry, {guess} is not in the word. Try again.")
    # Ask the user to guess a letter
    guess = input("Guess a letter: ")

    # Check that the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        # If the guess passes the checks, break out of the loop
        break
    else:
        # If the guess does not pass the checks, print a message
        print("Invalid letter. Please, enter a single alphabetical character.")