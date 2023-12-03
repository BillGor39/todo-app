import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
todo_label = sg.Text("")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[44, 10])
edit_button = sg.Button("Edit")
exit_button = sg.Button("Exit")

window = sg.Window("My To-do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, value = window.read()

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value["todo"].capitalize() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            new_todo = value["todo"].capitalize() + "\n"
            todo = value["todos"][0]
            todos = functions.get_todos()
            index = todos.index(todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break


window.close()
