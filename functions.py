FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """ Read a text file and return the list of
    to-do items."""
    # with context manager - file doesn't need to be closed
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(type(__name__))
# print(__name__)


if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())


def count(phrase):
    return phrase.count('.')