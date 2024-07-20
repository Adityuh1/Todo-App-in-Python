import functions
import FreeSimpleGUI as ui

label = ui.Text("Type in my TODO")
input_box = ui.InputText(tooltip="Enter To-Do", key='todo')
add_button = ui.Button("Add")
list_box = ui.Listbox(values=functions.get_todo(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = ui.Button("Edit")

window = ui.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 10))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'])
        case ui.WINDOW_CLOSED:
            break

window.close()