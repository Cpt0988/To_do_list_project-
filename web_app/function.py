
def get_todos(filepath="todos.txt"):
    try:
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
    except FileNotFoundError:
        todos_local = []  # Start with an empty list if file doesn't exist
    return todos_local


def write_todos(todos_arg,filepath="todos.txt"):
    with open(filepath,'w') as file:
            file.writelines(todos_arg)
        
#