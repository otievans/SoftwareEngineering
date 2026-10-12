def add_note():
    print('---Note entry mode---')
    while True:
        note_content = input("Enter your note(Click 'e' to exit  : ").strip()
        if note_content=='e' :
            print('Done')
            break

        if note_content :
            with open('Notes.txt', 'a') as file :
                file.write(note_content + '\n')
            print('Noted saved successfully.')
        else :
            print('Note cannot be empty')

def clear_whole_file() :
    with open('Notes.txt', "w") as file :
        pass
    print("All notes have been cleared successfully.")

def clear_single_line():
    try :
        with open("Notes.txt", 'r') as file :
            lines= file.readlines()
        if not lines :
            print("Your note is Empty.")
            return

        print("\n---Current Notes---")
        for index, line in enumerate(lines, start=1) :
            print(f'{index}, {line.strip()}')

        choice = input('Enter the line number you want to delete(or type exit)')
        if choice == 'exit' :
            return
        line_num = int(choice)
        if 1 <= line_num <= len(lines):
            removed  = lines.pop(line_num - 1)
            with open('Notes.txt', 'w') as file :
                file. writelines(lines)
            print(f'Deleted note: {removed.strip()}')
        else :
            print('Invalid line number')
    except FileNotFoundError :
        print('No notes file found yet.')
    except ValueError :
        print('Please enter a valid number')

def view_notes():
    try:
        with open('Notes.txt', 'r') as file :
            notes = file.readlines()
            if notes :
                for index, note in enumerate(notes, start=1) :
                    print(f'{index}, {note.strip()}')
                    return
            else :
                print('No notes found!!')
    except FileNotFoundError :
        print('No file found, Create a new one.')




