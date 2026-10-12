from notes import add_note
from notes  import clear_whole_file
from notes  import clear_single_line
from notes import view_notes
print('=== Personal CLI Utility ===')

name= input('What is your name?  ')
print(f'Hello, {name}')
while True:
    print('options'
          '\n1. calculate '
          '\n2. take a note'
          '\n3. exit')

    while True :
         choice= input("what do you want to do( '1','2', '3',)  ")
         if choice in [ '1', '2' ,'3' ] :
             break
         else :
             print('Invalid Choice!!, pick either 1 ,2 or 3')

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


    elif choice == "2" :
        print('--Notes Main Menu--'
              '\n 1. Add a note' 
              '\n 2. Clear all notes'
              '\n 3. Clear single line ' 
              '\n 4. View notes')

        option2 = input('What would you like to do? ')
        if option2 =="1" :
            add_note()
        elif option2 == '2' :
            clear_whole_file()
        elif option2 == '3' :
            clear_single_line()
        elif option2 =="4" :
            view_notes()
    elif choice ==  '3' :
        print('You have exited successfully.')
        break



    