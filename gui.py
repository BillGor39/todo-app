import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")
clock_label = sg.Text(key="clock")
input_label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(image_size=(50, 30), mouseover_colors="LightBlue2",
                       tooltip="Add to do", image_source=functions.resource_path("add.png"), key="Add")
todo_label = sg.Text("")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=(44, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_size=(60, 50), mouseover_colors="LightBlue2", tooltip="complete",
                            image_source=functions.resource_path("complete.png"), key="Complete")
message_label = sg.Text(key="message")
exit_button = sg.Button("Exit")

window = sg.Window("My To-do App",
                   layout=[[clock_label],
                           [input_label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button, message_label]],
                   font=("Helvetica", 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"].capitalize().strip(" ") + "\n"
            if new_todo != "\n":
                todos.append(new_todo)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            else:
                sg.popup("Cannot add empty todo.")

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"].capitalize().strip(" ") + "\n"
                if new_todo != "\n":
                    todos = functions.get_todos()
                    index = todos.index(todo_to_edit)
                    todos[index] = new_todo
                    functions.write_todos(todos)
                    window["todos"].update(values=todos)

                else:
                    sg.popup("cannot edit to empty todo.")
            except IndexError:
                # window["message"].update("choose a todo to edit.")
                sg.popup("Choose a todo to edit.", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todo"].update(value="")
                window["todos"].update(values=todos)
            except IndexError:
                # window["message"].update("choose a todo to complete.")
                sg.popup("Choose a todo to complete.", font=("Helvetica", 20))

        case "todos":
            try:
                window["todo"].update(value=values["todos"][0].strip("\n"))
            except IndexError:
                continue

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break


window.close()
