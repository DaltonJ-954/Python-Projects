Name = input('Please enter the name of the person who created this game')
print('This game was made by tghe amazing ' + Name + '!')
print('Welcome to my guessing game!')
print('In this program, you will try to guess a word that I chose.')
print('Good luck!')

def start():
    Player_Name = input('What is  the name of the player? ')
    print('Greetings, ' + Player_Name + '! It is time to guess!')
    Secret_Word = 'Playstation'.lower()
    Guesses = ''
    Turns_Left = 8
    while Turns_Left > 0:
        Wrong_Answer = 0
        for Letter in Secret_Word:
            if Letter in Guesses:
                print(Letter)
            else:
                print('_')
                Wrong_Answer += 1
        if Wrong_Answer == 0:
            print('YOU WIN! You guessed my word: ' + Secret_Word + '!!!!!')
            break
        Guess = input('Guess a letter here: ').lower()
        Guesses += Guess

        if Guess not in Secret_Word:
            Turns_Left -= 1
            print('Oops! This letter is not in my word. Please try again.')
            print('You have ' + str(Turns_Left) + ' more guesses left. You can do it!')
            if Turns_Left == 0:
                print('GAME OVER')

    def Play_Again():
        Again = input('Would you like to play again? ').lower()
        if Again == 'No'.lower():
            quit()
        if Again == 'Yes'.lower():
            start()
        else:
            print('Please enter Yes or No. Thank you!')
            Play_Again()

start()
            

        
