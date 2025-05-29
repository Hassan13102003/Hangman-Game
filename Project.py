import random
from hangman_words import word_list
from hangman_art import stages, hangman
# HangMan Game

print(hangman)
choosen_word=random.choice(word_list)
print(choosen_word)

placeholder=""
for pos in range(0, len(choosen_word)):
    placeholder+="_"
print(placeholder)

game_over=False
correct_list=[]
lives=6
while not game_over:
    print(f"No. of lives left:{lives}")

    guess=input("Guess a letter:").lower()

    if guess in correct_list:
        print(f"{guess} already guessed")
    display=""

    for letter in choosen_word:
        if letter==guess:
            display+=letter
            correct_list.append(letter)
        elif letter in correct_list:
            display+=letter
        else:
            display+="_"
    if guess not in choosen_word:
        lives-=1
        print(f"you guessed {guess}, that is not in the word")
        if lives==0:
            game_over=True
            print(f"You lose, The correct word was {choosen_word}")

    print(display)
    if "_" not in display:
        print("You win")
        game_over = True
    print(stages[lives])

