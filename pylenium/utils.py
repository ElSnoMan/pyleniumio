import pathlib


def read_script_from_file(file_name) -> str:
    """ Get the script string from a file in the scripts directory.

    Args:
        file_name: The file name with extension to read from.

    Examples:
        script = read_script_from_file('drag_and_drop.js')
    """
    path = str(pathlib.Path(__file__).parent.absolute())
    with open(path + f'/scripts/{file_name}', 'r') as file:
        script = file.read()
    return script
