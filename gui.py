import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
todo_label = sg.Text("")
exit_button = sg.Button("Exit")

window = sg.Window("My To-do App",
                   layout=[[label],
                           [input_box, add_button],
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
        case sg.WIN_CLOSED:
            break


window.close()
