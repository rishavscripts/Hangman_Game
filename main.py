print("Welcome to The Hangman Game.")
print("Guess the word before the structure completes and lives are gone.")
print("Hint: Country name. ")
words=['Canada','India','Italy','Australia','England']
lives=7
import random
import hangman_stages
word=random.choice(words)

display=[]
for i in range(len(word)):
    display+='_'
print(display)
flag=True
while flag:
    letter=input("Enter your letter: ")
    if letter in word:
        print(f"Right guess. {lives} lives remaining.")
        for pos in range(len(word)):
            if letter==word[pos]:
                display[pos]=letter
        print(display)
        print(hangman_stages.stages[lives])

    if letter not in word:
        lives-=1
        print(f"Wrong guess, {lives} lives remaining.")
        print(display)
        print(hangman_stages.stages[lives])
        if lives==0:
            print("You loose.")
            flag=False

    if '_' not in display:
        print(display)
        print("You guessed it right. Game over. You win.")
        flag=False