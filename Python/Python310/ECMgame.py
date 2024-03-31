def start():
    print('This is my Eleplant Cat and Mouse Game!')
    Player_One = 'Elton'
    Player_Two = 'Paul'

    def choices(Player_One_Choice, Player_Two_Choice):
        if Player_One_Choice == 'eleplant' and Player_Two_choice == 'mouse':
            return('Mouse covers Eleplant! ' + Player_Two + ' wins!')
        elif Player_One_Choice == 'mouse' and Player_Two_Choice =='elephant':
            return('Mouse covers Elephant! ' + Player_One + ' wins!')
        elif Player_One_Choice == 'cat' and Player_Two_Choice == 'mouse':
            return('Cat cuts Mouse! ' + Player_One + 'wins!')
        elif Player_One_Choice == 'elephant' and Player_Two_Choice == 'cat':
            return('Elephant smashes Cat! ' + Player_One + ' wins!')
        elif Player_One_Choice == 'mouse' and Player_Two_Choice == 'cat':
            return('Cat cuts Mouse! ' + Player_Two + 'wins!')
        elif Player_One_Choice == 'cat' and Player_Two_Choice == 'elephant':
            return('Elephant smashes Cat! ' + Player_Two + ' wins')
        elif Player_One_Choice == Player_Two_Choice:
            return('Jack and Erik tied!')
        else:
            return('Please type Elephant, Mouse, or Cat!')
    Player_One_Choose = input('Does ' + Player_One +
                              ' choose Elephant, Mouse, or Cat? ').lower()
    Player_Two_Choose = input('Does ' + Player_Two +
                              ' choose Elephant, Mouse, or Cat? ').lower()
    print(choices(Player_One_Choose, Player_Two_Choose))

    def Play_Again():
        Again = input('Would you like to play the game again? ').lower()
        if Again == 'No'.lower():
            quit()
        if Again == 'Yes'.lower():
            start()
        else:
            print('Pleas enter Yes or No. Thank you!')
            Play_Again()
    Play_Again()
start()
                   
