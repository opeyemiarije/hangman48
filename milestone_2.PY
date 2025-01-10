import random

#Create a list containing the names of your 5 favorite fruits
favorite_fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Assign this list to a variable called word_list
word_list = favorite_fruits

# Print out the newly created list to the standard output (screen)
print(word_list)
word = random.choice(word_list)
print(word)
# Ask the user to enter a single letter
guess = input("Enter a single letter: ")

# Assign the input to a variable called guess
print(f"You guessed: {guess}")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")