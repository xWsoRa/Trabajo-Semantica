import random

# Define a list of possible fill-in-the-gap sentences
sentences = [
    "The quick brown ____ jumps over the lazy dog.",
    "I ____ therefore I am.",
    "In the beginning God created the ____ and the earth.",
    "To be or not to be, that is the ____.",
    "It is not in the ____ of stars to hold our destiny, but in ourselves.",
    "The only way to do great work is to love what you ____.",
    "Ask not what your country can do for you, ask what you can do for your ____."
]

# Define a function to select a random sentence and remove a random word
def select_sentence():
    sentence = random.choice(sentences)
    words = sentence.split()
    index = random.randint(0, len(words) - 1)
    word = words[index]
    words[index] = "___"
    gap_sentence = " ".join(words)
    return (word, gap_sentence)

# Define a function to prompt the user to fill in the gap and check their answer
def play_game():
    word, gap_sentence = select_sentence()
    print(gap_sentence)
    user_input = input("Fill in the gap: ")
    if user_input.lower() == word.lower():
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer was {word}.")

# Play the game
play_game()
