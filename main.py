
print('=== Personal CLI Utility ===')

name= input('What is your name?  ')
print(f'Hello, {name}')
print('options'
      '\n1. calculate '
      '\n2. take a note'
      '\n3. exit')


choice= input("what do you want to do ")
if choice=="1" :
    print('====Calculator====')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Back to Main Menu')


while True :
    try:
        option= int(input('What would you like to do?(1,2,3,4)'))
        if option in [1,2,3,4] :
            break
        else:
            print('Invalid option, Please enter 1,2,3 or 4.')
    except ValueError:
        print('Invalid input, Please enter a number.')

while True :
    try:
        num1 = float(input('Enter the first number'))
        break
    except ValueError :
        print("Input must be a number ")


while True :
    try :
        num2 = float(input('Enter the second number'))
        break
    except ValueError:
        print("Input must be a number")


if option == 1 :
    print(num1 + num2)

elif option == 2 :
            print( num1 - num2)
elif option== 3 :
            print(num1 * num2)
elif option == 4 :
 if num2 ==0:
            print("Error!!: cannot divide by zero")
 else :
            print( num1/num2)

else :
            print('Invalid Operation')


