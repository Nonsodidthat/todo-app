def get_tasks(filepath='App.txt'):
    """
    Read a text file and return a list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local

def write_tasks(tasks_arg, filepath='App.txt',):
    """ Write the to-do items list in a text file"""
    with open('App.txt', 'w') as file_here:
        file_here.writelines(tasks_arg)