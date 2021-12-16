# print welcome message
print('Welcome to the Letter Counter App\n')

# get input from the user
name = input('What is your name: ').title().strip()
print(f'\nHello {name}!')
print('I will count the number of times that a specific letter occurs in a message.\n')

# make every character lower case
message = input('Please enter a message: ').lower()
letter = input('Which letter would you like to count the occurences of: ').lower()

# count the number of given letter
count_of_letter = message.count(letter)

print(f'{name}, your {count_of_letter} {letter}\'s in it.')
