def start():
    people_dictionary = {'brett' : ['Male', 'Weright 175'], 'nancy' : ['Female', 'Weight 125'], 'patrick' : ['Male', 'Weight 195'], 'briar' : ['Female', 'Weight 115'], 'adam' : ['Male', 'Weight 215']}




    Name = input('Please type in a name: ').lower()
    print('You typed in the name ' + Name.capitalize())
    try:
        Persons_data = people_dictionary[Name]
        print('Name: ' + Name.capitalize())
        print('Sex: ' + Persons_data[0])
        print('Weight: ' + Persons_data[1])
        more()
    except:
        print('That name (as written) was not found in the dictionary.')
        more()
def more():
    More = input('Would you like to search for another name? ')
    if More == 'No' :
        quit()
    if More == 'Yes' :
        start()
    else:
        print('Please enter Yes or No.')
        more()
start()
