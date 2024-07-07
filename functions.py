FILEPATH = "todos.txt"

def get_todo(filepath = FILEPATH):
    """READS THE FILE AND RETURNS THE TODO LIST."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath = FILEPATH):
    """Writes To-Do items list in a text file."""
    with open(filepath, 'w') as file_local2:
        file_local2.writelines(todos_arg)

if __name__  == "__main__":
    print(get_todo())