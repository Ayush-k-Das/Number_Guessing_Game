import random

multi_line_string1 = """Welcome to the Number Guessing Game!
    I'm thinking of a number between 1 and 100.
    Your chances to guess the correct number will depend on your defficulty level.."""
print(multi_line_string1)

multi_line_string2 = """Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances) """
print(multi_line_string2)

choice=input('Enter your choice (1/2/3) to play or (exit) to quit playing: ')
if choice=='1':
    print("""Great! You have selected the Easy difficulty level.
          You will be getting 10 chances to guess the correct number.
          Let's start the game!""")
    
    chance=10
    attempt=0
    num=random.randint(1,100)
    while chance>attempt:
        attempt+=1
        guess=int(input('Guess the number: '))
        if guess==num:
            print(f'Congratulations! You have guessed the correct number {num} in {attempt} attempts.')
            break
        elif chance==attempt and guess!=num:
            print(f'Sorry! The number was {num}. Better luck next time.')
        elif guess>num:
            print(f'Incorrect! The number is smaller than {guess}.')
        elif guess<num:
            print(f'Incorrect! The number is greater than {guess}.')

elif choice=='2':
    print("""Great! You have selected the Medium difficulty level.
          You will be getting 5 chances to guess the correct number.
          Let's start the game!""")

    chance=5
    attempt=0
    num=random.randint(1,100)
    while chance>attempt:
        attempt+=1
        guess=int(input('Guess the number: '))
        if guess==num:
            print(f'Congratulations! You have guessed the correct number {num} in {attempt} attempts.')
            break
        elif chance==attempt and guess!=num:
            print(f'Sorry! The number was {num}. Better luck next time.')
        elif guess>num:
            print(f'Incorrect! The number is smaller than {guess}.')
        elif guess<num:
            print(f'Incorrect! The number is greater than {guess}.')

elif choice=='3':
    print("""Great! You have selected the Hard difficulty level.
          You will be getting 3 chances to guess the correct number.
          Let's start the game!""")

    chance=3
    attempt=0
    num=random.randint(1,100)
    while chance>attempt:
        attempt+=1
        guess=int(input('Guess the number: '))
        if guess==num:
            print(f'Congratulations! You have guessed the correct number {num} in {attempt} attempts.')
            break
        elif chance==attempt and guess!=num:
            print(f'Sorry! The number was {num}. Better luck next time.')
        elif guess>num:
            print(f'Incorrect! The number is smaller than {guess}.')
        elif guess<num:
            print(f'Incorrect! The number is greater than {guess}.')

elif choice.lower()=='exit':
    print('Thanks for playing the game!')

else:
    print('Enter a valid choice from (1/2/3)')


    





