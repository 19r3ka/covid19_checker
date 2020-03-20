import os

def clear_console():
    """ Clears the python command line console """
    # cls on Windows and clear on Linux and Mac
    command = "cls" if os.name == "nt" else "clear"
    return os.system(command)