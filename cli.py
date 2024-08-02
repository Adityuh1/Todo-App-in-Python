# from functions import get_todo,write_todo
import time

import functions

this = time.strftime("%b %d , %Y %H:%M:%S")
print("It is", this)

while True:
    prompt = input("Enter from the following commands"
                   "'add','show','edit','complete' or 'exit':")
    prompt = prompt.strip()

    if prompt.startswith("add"):
        todo = prompt[4:]

        todos = functions.get_todo()

        todos.append(todo + "\n")

        functions.write_todo(todos)

    elif prompt.startswith("show"):
        todos = functions.get_todo()

        for index, items in enumerate(todos):
            items = items.strip('\n')
            row = f"{index + 1}-{items}"
            print(row)

    elif prompt.startswith("edit"):
        try:
            number = int(prompt[5:])
            number = number - 1

            todos = functions.get_todo()

            new_todo = input("Enter new todo:")
            todos[number] = new_todo

            functions.write_todo(todos)

        except ValueError:
            print("Your command is invalid! ")
            continue

    elif prompt.startswith("complete"):
        try:
            number = int(prompt[9:])

            todos = functions.get_todo()

            index = number - 1
            todos_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todo(todos)

            message = f"THE TODO '{todos_to_remove}' has been completed!"
            print(message)
        except IndexError:
            print("There is no item with that number! ")
            continue

    elif prompt.startswith("exit"):
        break

    else:
        print("You have entered an unknown command!")

print("Byeeeeeee!")