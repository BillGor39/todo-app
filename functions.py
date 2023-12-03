FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """get the todos from the file path
       and return the todos in a list"""
    with open(filepath, "r") as local_file:
        todos_local = local_file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items in the text file"""
    with open(filepath, "w") as local_file:
        local_file.writelines(todos_arg)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
