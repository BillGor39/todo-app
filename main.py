# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    action = input("Type add, show, edit, complete, clear or exit: ").lower()

    if action.startswith("add"):
        todo = action[4:]
        if todo == "":
            todo = input("Enter a todo: ")
        todo += "\n"

        todos = functions.get_todos()

        todos.append(todo.capitalize())

        functions.write_todos(todos)

        print(f"{todo.strip("\n")} is added.")

    elif action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = "{} -{}".format(index+1, item.strip("\n"))  # take the "\n" off from each todo
            print(row)

    elif action.startswith("edit"):
        try:
            number = action[5:]
            if number == "":
                number = input("Enter the number of todo to edit: ")
            number = int(number) - 1

            todos = functions.get_todos()

            todos_length = len(todos)

            # catch an error when the index of todo is out of range
            if number <= todos_length:
                new_todo = input("Enter a new todo: ").capitalize() + "\n"
                todos[number] = new_todo
                functions.write_todos(todos)
            else:
                print(f"the number is out of index. max is {todos_length}")

        except ValueError:
            print("Command is not valid. Try 'Edit (number)'")
            continue

    elif action.startswith("complete"):
        try:
            index = action[9:]
            if index == "":
                index = input("Enter the number of todo to complete: ")
            index = int(index) - 1
            todos = functions.get_todos()

            remove_todo = todos[index]
            todos.pop(index)

            functions.write_todos(todos)
            print(f"{remove_todo.strip("\n")} is removed.")
        except IndexError:
            print("number is out of the range.")
            continue
        except ValueError:
            print("Command is not valid. Try 'complete (number)'")

    elif action.startswith("exit"):
        break

    elif action.startswith("clear"):
        functions.write_todos("")
        print("The file has been cleared.")

    else:
        print("I don't understand. Try again\n")

print("Bye!")


