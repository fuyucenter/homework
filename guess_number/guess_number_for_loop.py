#Generate a random number (0 to 100) and ask the user to guess that number. 
# User has 5 tries to find the exact number. 
# The app will let the user know if his guess is too high or too low if incorrect. 

from random import randint

system_generate_number = randint(1, 100)
print(system_generate_number)

def get_user_number():
    user_number = int(input('Guess an integer number: '))
    return user_number

for i in range(5):
    user_input_number = get_user_number()
    if user_input_number > system_generate_number:
        print('The number you input is big')
    elif user_input_number < system_generate_number:
        print('The number you input is small')
    else:
        print('Bingo! You are right, the number is {}'.format(system_generate_number))
        break