print('Welcome to the Letter Counter App\n')
name = input('What is your name: ')
print(f'\nHello {name}!')
print('I will count the number of times that a specific letter occurs in a message.\n')
message = input('Please enter a message: ')
letter = input('Which letter would you like to count the occurences of: ')
count_of_letter = message.lower().count(letter)
print(f'{name}, your {count_of_letter} {letter}\'s in it.')
