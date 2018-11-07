from random import randint

system_generate_number = randint(1,100)
print(system_generate_number)

def user_number():
    number = int(input('Please guess a number:'))
    return number

while True:
    try:
        user_input_number = user_number()
    except ValueError as error:
        print('Please input integer number')
        continue
        #put continue here, when there is exception, go back "While" restart app
    if user_input_number > system_generate_number:
        print('The number you input is big')
    elif user_input_number < system_generate_number:
        print('The number you input is small')
    else:
        print('Bingo! You correct!')
        break
