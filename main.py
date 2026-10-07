print('=== Personal CLI Utility ===')

name= input('What is your name?  ')
print(f'Hello, {name}')

print('\nWhat would you like to do?')
print('1. Calculate ')
print('2. Take a note ')
print('3. Exit')

choice= input('choose an option ')

if choice =="1":
    print('Calculator selected')
elif choice == '2' :
    print('Take a note selected')
elif choice == '3' :
    print('Exit selected')
else :
    print('Invalid Choice!!\nChoice should be a number listed above')